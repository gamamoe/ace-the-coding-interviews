class PriorityQueue {
  constructor() {
    this.values = [];
  }
  enqueue(val, priority) {
    this.values.push({ val, priority });
    this.sort();
  }
  dequeue() {
    return this.values.pop();
  }
  sort() {
    this.values.sort((a, b) => b.priority - a.priority);
  }
}

module.exports = { PriorityQueue };
