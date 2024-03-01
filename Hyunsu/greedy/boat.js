/**
 * 투포인터를 이용한 풀이 
 * 최대 2명이고, limit에 최대한 가깝게 만들기 가장 무거운 사람과 가장 가벼운 사람을 같이 태우기 
 * 시간복잡도 : O(N)
 * @param {*} people 
 * @param {*} limit 
 * @returns 
 */
function solution(people, limit) {
    var answer = 0;
    let left = 0;
    let right = people.length-1;
    people.sort((a,b)=>a-b)
    //투포인터 
    while(left<right){
        // 두명이 같이 탈 수 있는 조건 : 둘의 합이 limit보다 작거나 같아야함
        // 같이 탈 수 있으면 left와 right를 한칸씩 옮겨줌
        if(people[left] + people[right] <= limit){
            answer+=1
            left+=1;
            right-=1;
        }else{
            //같이 탈 수 없는 경우 : limit을 넘는 경우 
            // 더 작은 사람을 태워야 함 . 
            // right를 옮기면서, 큰 사람은 혼자 타게 함 
            right-=1;
            answer+=1
        }    
    }
    // 마지막 남은 한명 태우기
    if(left===right){
        answer+=1
    }
    return answer
}

console.log(solution([70, 50, 80, 50],100)) //3
console.log(solution([70, 80, 50],100)) //3