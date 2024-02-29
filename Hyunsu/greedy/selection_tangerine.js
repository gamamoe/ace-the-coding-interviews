/**
 * 종류의 수를 최소화. 
 * -> 많은 개수를 가진 종류 부터 선택 해보기
 * 
 * @param {*} k 
 * @param {*} tangerine 
 * @returns 
 */
function solution(k, tangerine) {
    let cnt =0;
    // mapper
    const mapper = {}
    //귤의 종류별로 개수 세기 
    tangerine.forEach((t)=> mapper[t]=(mapper[t]||0)+1)
    // sort 내림차순 - 종류의 수를 최소화하기 위해 많은 개수를 가진 종류부터 선택하기 위해 
    const sortedMapper =Object.entries(mapper).sort((a,b)=>b[1]- a[1])
    // loop하면서
    for (const [_, t] of sortedMapper){
        k-=t // 귤 담기 
        cnt+=1 // 종류 수 증가 
        if(k<=0) break // 귤 다 담았으면 종료
    }    
    return cnt;
}

console.log(solution(5, [3, 1, 4, 1, 5])) //3
console.log(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) //3