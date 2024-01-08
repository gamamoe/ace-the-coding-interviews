class Queue {
  #queue = {};

  constructor() {
    this.tail = 0;
    this.head = 0;
  }
  display() {
    return this.#queue;
  }
  // queue의 마지막 자리
  enqueue(ele) {
    this.#queue[this.tail++] = ele;
  }

  /**
   * Queue의 첫번째 요소 가져오기
   * 첫번째 요소를 가져온 후, 빈 공간을 리스트에서 지우기 위해 delete 를 사용.
   * @returns {*} Queue에 첫번째 요소가 있을 경우 요소 반환, 비어 있을 경우 null을 반환
   */
  dequeue() {
    if (this.tail === this.head) return null;
    const element = this.#queue[this.head];
    delete this.#queue[this.head++];
    return element;
  }

  length() {
    return Object.keys(this.#queue).length;
  }

  icrSort() {
    if (!this.length()) return this.#queue;
    return Array.isArray(this.#queue[1])
      ? [...Object.entries(this.#queue)].sort((a, b) => a[1][0] - b[1][0])
      : [...Object.entries(this.#queue)].sort((a, b) => a[1] - b[1]);
  }
  descSort() {}
}

module.exports = Queue;
