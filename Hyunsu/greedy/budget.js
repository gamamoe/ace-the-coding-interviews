// Url: https://programmers.co.kr/learn/courses/30/lessons/12982
//  Date: 2021-07-07 Wed
// 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때,
// 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.
// 최대 많은 부서에 물품 지원  -> 적게 요청한 예산 순으로 정렬 -> 예산이 남아있는 동안 요청한 예산을 더함
// 현재 사용한 예산이 주어진 예산 보다 작으면 부서의 수++
// 현재 사용한 예산이 주어진 예산 보다 크면 종료한다.
function solution(d, budget) {
  return d
    .sort((a, b) => a - b)
    .reduce((cnt, b) => {
      return (cnt += (budget -= b) >= 0);
    }, 0);
  return cnt;
}

console.log(solution([1, 3, 2, 5, 4], 9)); //3
console.log(solution([2, 2, 3, 3], 10)); //4
