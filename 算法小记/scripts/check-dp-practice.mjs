import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8').replace(/^\uFEFF/, '').replace(/\r\n/g, '\n');
const planPath = '05-题单/Codeforces/DP分知识点题单.md';
const plan = read(planPath);
const template = read('99-模板/题目卡片模板.md');
const requiredKeys = [...template.matchAll(/^([a-z_]+):/gm)].map(match => match[1]);
const requiredHeadings = ['题意摘要', '识别信号', '状态与转移', '复杂度', 'Rust 实现', '复盘'];
const statuses = new Set(['todo', 'doing', 'solved', 'redo', 'mastered']);
const priorities = new Set(['core', 'important', 'challenge']);

function scalar(value) {
  if (value.startsWith('"')) return JSON.parse(value);
  if (value.startsWith("'") && value.endsWith("'")) return value.slice(1, -1).replace(/''/g, "'");
  return value;
}

// Problem cards use the template's flat, single-line frontmatter fields.
function frontmatter(text, file) {
  const match = text.match(/^---\n([\s\S]*?)\n---(?:\n|$)/);
  assert(match, `${file}: missing frontmatter`);
  const fields = {};
  for (const line of match[1].split('\n')) {
    if (!line.trim()) continue;
    const entry = line.match(/^([a-z_]+):[ \t]*(.*)$/);
    assert(entry, `${file}: unsupported frontmatter line ${line}`);
    assert(!Object.hasOwn(fields, entry[1]), `${file}: duplicate field ${entry[1]}`);
    fields[entry[1]] = scalar(entry[2].trim());
  }
  return fields;
}

function links(text) {
  return [...text.matchAll(/\[\[([^\]]+)\]\]/g)].map(match => {
    const [target, alias] = match[1].replace(/\\\|/g, '|').split('|');
    assert(!target.includes('../'), `Non-relative WikiLink: ${target}`);
    return { target: target.replace(/\.md$/, ''), alias };
  });
}

function section(text, title, depth = 2) {
  const heading = `${'#'.repeat(depth)} ${title}`;
  const lines = text.split('\n');
  const start = lines.indexOf(heading);
  assert(start >= 0, `Missing heading: ${heading}`);
  let end = start + 1;
  while (end < lines.length && !new RegExp(`^#{1,${depth}} `).test(lines[end])) end++;
  return lines.slice(start + 1, end).join('\n');
}

const cards = new Map();
const byTarget = new Map();
for (const name of fs.readdirSync(path.join(root, '04-题库/Codeforces'))) {
  if (!name.endsWith('.md')) continue;
  const file = `04-题库/Codeforces/${name}`;
  const text = read(file);
  const fields = frontmatter(text, file);
  assert.deepEqual(Object.keys(fields).sort(), [...requiredKeys].sort(), `${file}: template fields differ`);
  assert.equal(fields.type, 'problem', file);
  assert.equal(fields.platform, 'Codeforces', file);
  assert(/^\d+[A-Z]\d*$/.test(fields.problem_id), `${file}: invalid Codeforces ID`);
  assert(statuses.has(fields.status), `${file}: invalid status`);
  assert(priorities.has(fields.priority), `${file}: invalid priority`);
  assert(Number(fields.rating) > 0, `${file}: missing rating`);
  for (const heading of requiredHeadings) section(text, heading);
  assert(!cards.has(fields.problem_id), `Duplicate problem: ${fields.problem_id}`);
  const card = { ...fields, file, target: file.slice(0, -3), text };
  cards.set(card.problem_id, card);
  byTarget.set(card.target, card);
}

function exerciseIds(text, context) {
  return links(text).filter(link => link.target.startsWith('04-题库/')).map(link => {
    assert(link.target.startsWith('04-题库/Codeforces/'), `${context}: non-Codeforces exercise`);
    const card = byTarget.get(link.target);
    assert(card, `${context}: missing card ${link.target}`);
    return card.problem_id;
  });
}

const units = [];
for (const row of section(plan, '题量安排').split('\n')) {
  const match = row.match(/^\| (\[\[.*?\]\]) \| ([^|]+) \| (\d+) \| (\d+) \|$/);
  if (row.startsWith('| [[')) assert(match, `Malformed quota row: ${row}`);
  if (!match) continue;
  const [link] = links(match[1]);
  assert(link.alias, `Quota row needs an alias: ${row}`);
  units.push({ note: link.target, name: link.alias, importance: match[2].trim(), target: +match[3], count: +match[4] });
}
assert(units.length > 0, 'No quota rows found');
assert.equal(new Set(units.map(unit => unit.name)).size, units.length, 'Duplicate unit names');

const used = new Set();
const notes = new Set();
const totalSet = read('05-题单/Codeforces/DP题单.md');
for (const unit of units) {
  assert(unit.target >= 4, `${unit.name}: target below four`);
  const ids = exerciseIds(section(plan, unit.name), unit.name);
  assert.equal(new Set(ids).size, ids.length, `${unit.name}: duplicate exercises`);
  assert.equal(ids.length, unit.count, `${unit.name}: quota table count is stale`);
  assert(ids.length >= unit.target, `${unit.name}: not enough exercises`);
  const note = read(`${unit.note}.md`);
  const heading = `${unit.name}（${unit.importance}，${unit.count} 题）`;
  assert.deepEqual(exerciseIds(section(note, heading, 3), unit.note), ids, `${unit.name}: note differs from plan`);
  assert.deepEqual(exerciseIds(section(totalSet, unit.name), 'DP题单'), ids, `${unit.name}: total set differs`);
  for (const id of ids) used.add(id);
  notes.add(unit.note);
}
for (const note of notes) {
  const headings = [...section(read(`${note}.md`), '典型题目').matchAll(/^### (.*)$/gm)].map(match => match[1]);
  const expected = units.filter(unit => unit.note === note).map(unit => `${unit.name}（${unit.importance}，${unit.count} 题）`);
  assert.deepEqual(headings, expected, `${note}: practice units differ from the quota table`);
}

const dpDir = path.join(root, '03-算法/动态规划');
function checkConceptCoverage(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) checkConceptCoverage(file);
    else if (entry.name.endsWith('.md') && !entry.name.startsWith('00-')) {
      const relative = path.relative(root, file).replaceAll(path.sep, '/').slice(0, -3);
      assert(notes.has(relative), `${relative}: no exercise quota`);
    }
  }
}
checkConceptCoverage(dpDir);

const board = read('00-索引/题目状态看板.md');
const boardIds = new Set();
for (const row of board.split('\n').filter(line => /^\| \[\[04-题库\//.test(line))) {
  const [id] = exerciseIds(row, 'status board');
  const columns = row.replace(/\[\[[^\]]+\]\]/, 'CARD').split('|').map(value => value.trim());
  const card = cards.get(id);
  assert(!boardIds.has(id), `${id}: duplicate board row`);
  assert.equal(Number(columns[2]), Number(card.rating), `${id}: board rating differs`);
  assert.equal(columns[3], card.priority, `${id}: board priority differs`);
  assert.equal(columns[4], card.status, `${id}: board status differs`);
  boardIds.add(id);
}
for (const id of used) assert(boardIds.has(id), `${id}: missing board row`);
assert(!used.has('455B'), '455B is Trie game DP, not bitmask DP');

const levels = [
  ['05-题单/Codeforces/DP基础题单.md', rating => rating <= 2000],
  ['05-题单/Codeforces/DP进阶题单.md', rating => rating > 2000],
];
const leveled = new Set();
for (const [file, accepts] of levels) {
  for (const id of exerciseIds(read(file), file)) {
    assert(used.has(id), `${file}: exercise outside main plan ${id}`);
    assert(!leveled.has(id), `${file}: duplicate exercise ${id}`);
    assert(accepts(Number(cards.get(id).rating)), `${file}: rating band mismatch ${id}`);
    leveled.add(id);
  }
}
assert.deepEqual([...leveled].sort(), [...used].sort(), 'Leveled sets do not cover the main plan');

for (const file of [
  '00-索引/算法总览.md', '00-索引/DP路线图.md',
  '03-算法/动态规划/00-DP总览.md', '03-算法/动态规划/02-背包DP/00-背包DP总览.md',
]) {
  assert(links(read(file)).some(link => `${link.target}.md` === planPath), `${file}: missing practice entry`);
}
const overviewLinks = links(read('00-索引/算法总览.md'));
for (const name of ['DP路线图', '线段树路线图', '树状数组路线图', '图论路线图']) {
  assert(overviewLinks.some(link => link.target === name || link.target === `00-索引/${name}`), `Missing roadmap: ${name}`);
  assert(fs.existsSync(path.join(root, '00-索引', `${name}.md`)), `Missing roadmap file: ${name}`);
}

const snapshotFlag = process.argv.indexOf('--metadata');
if (snapshotFlag >= 0) {
  const source = process.argv[snapshotFlag + 1];
  assert(source, '--metadata requires an official Codeforces API JSON file');
  const response = JSON.parse(fs.readFileSync(source, 'utf8'));
  assert.equal(response.status, 'OK', 'Invalid Codeforces API snapshot');
  const official = new Map(response.result.problems.map(problem => [`${problem.contestId}${problem.index}`, problem]));
  let checked = 0;
  for (const id of used) {
    const card = cards.get(id);
    if (!card.text.includes('> 元数据核对：')) continue;
    const problem = official.get(id);
    assert(problem, `${id}: missing official metadata`);
    assert.equal(card.title, problem.name, `${id}: title differs from official snapshot`);
    assert.equal(Number(card.rating), problem.rating, `${id}: rating differs from official snapshot`);
    assert.deepEqual(JSON.parse(card.tags), problem.tags, `${id}: tags differ from official snapshot`);
    checked++;
  }
  console.log(`Official metadata checked: ${checked}`);
}

console.log(`DP practice: ${units.length} units, ${[...units].reduce((sum, unit) => sum + unit.count, 0)} entries, ${used.size} unique Codeforces problems`);
console.log('All quotas >= 4; cards, notes, sets, dashboard, and navigation agree.');
