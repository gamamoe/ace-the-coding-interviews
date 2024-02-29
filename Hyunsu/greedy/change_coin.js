function change_coin(amount){
    const answer = [];
    const changes = [1, 10, 50, 100]

    changes.sort((a,b)=> b-a)

    for(const c of changes){
        const count = Math.floor(amount/c);
        amount = amount % c;
        for(let i=0; i<count; i++){
            answer.push(c)
        }
    }
    return answer
}

console.log(change_coin(123))
console.log(change_coin(350)) 
