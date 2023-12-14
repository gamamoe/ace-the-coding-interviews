/**
 * 장르내에서 많이 재생된 노래 순서부터 
 * genreFeq =  {"classic": { freqSum: number, idx:number[], freq:[ {idx:1, freq:3 }]
 
 *  @param {*} genres 
 * @param {*} plays 
 * @returns 
 */
function solution(genres, plays) {
  const answer = [];
  const genresFreq = {};

  plays.forEach((freq, idx) => {
    const genreKey = genres[idx];

    genresFreq[genreKey] = {
      freqSum: (genresFreq[genreKey]?.freqSum || 0) + freq,
      idx: genresFreq[genreKey]?.idx
        ? [...genresFreq[genreKey].idx, idx]
        : [idx],
      freq: genresFreq[genreKey]?.freq
        ? [...genresFreq[genreKey].freq, { idx, freq }]
        : [{ idx, freq }],
    };
  });

  //일단 장르별로 sort
  const genresByFreqSum = Object.entries(genresFreq).sort((a, b) => {
    return b[1].freqSum - a[1].freqSum;
  });

  // 장르 내 idx 정렬
  for (const genre of genresByFreqSum) {
    const [name, { freqSum, idx, freq }] = genre;

    const idByFreq = freq.sort((a, b) => {
      if (a.freq > b.freq) return -1;
      if (b.freq < a.freq) return 1; // freq 내림차순
      return a.idx - b.idx; //같으면 오름차순
    });
    answer.push(idByFreq);
  }

  //높은 순의 2개 가져오기
  const result = [];
  for (const genre of answer) {
    for (let i = 0; i < 2; i++) {
      if (!genre[i]) break;
      result.push(genre[i].idx);
    }
  }

  return result;
}
