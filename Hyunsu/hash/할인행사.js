/**
 * 접근법:
 * 10일치의 아이템과 개수를 저장하는 map 생성(=currentDiscount)
 * sliding window로 10일치 부터 left 아이템을 빼주고, 현재 순회하는 아이템을 map(=currentDiscount)에 더해준다.
 * hasAllWantItem 함수를 통해 10일간의 아이템과 수량이, 사고싶은 리스트의 아이템과 수량이 일치하는지 확인
 * 만약 일치하면 answer +=1
 *
 *
 * Time Complexity: O(discount*want) = O(100000*10)= O(1000000) 백만
 *  discount 때마다 want를 순회하므로, want를 순회하는 시간복잡도를 줄여보기.

 * 
 * @param {*} want
 * @param {*} number
 * @param {*} discount
 * @returns
 */

function solution(want, number, discount) {
  var answer = 0;
  const currentDiscount = new Map();
  for (let i = 0; i < discount.length; i++) {
    const item = discount[i];
    if (i < 10) {
      currentDiscount.set(item, (currentDiscount.get(item) || 0) + 1);
      if (i === 9) {
        if (hasAllWantItem(want, currentDiscount, number)) {
          answer += 1;
        }
      }
      continue;
    }
    //11일차부터확인(i=10)
    //해당 day아이템 계산
    currentDiscount.set(item, (currentDiscount.get(item) || 0) + 1);
    //slidingwindow로 left 빼주기
    let left = i - 10;
    const leftItem = discount[left];
    currentDiscount.set(leftItem, currentDiscount.get(leftItem) - 1); //음수고려

    if (hasAllWantItem(want, currentDiscount, number)) {
      answer += 1;
    }
  }

  return answer;
}

function hasAllWantItem(want, currentDiscount, number) {
  let count = 0;
  for (let i = 0; i < want.length; i++) {
    //수량과, 아이템이 일치하는지
    if (
      currentDiscount.get(want[i]) &&
      currentDiscount.get(want[i]) === number[i]
    ) {
      //일치하면 +1
      count += 1;
    }
  }

  return count === want.length;
}
