def solution(id_list, report, k):
    answer = []
    reporter_dict = {}
    reported_dict = {}
    stopped = []
    mail_dict = {}
    for reporter_reported in report:
        reporter, reported = reporter_reported.split(" ")
        if reporter not in reporter_dict:
            reporter_dict[reporter] = []
        if reported not in reported_dict:
            reported_dict[reported] = []
        if reported not in reporter_dict[reporter]:
            reporter_dict[reporter].append(reported)
        if reporter not in reported_dict[reported]:
            reported_dict[reported].append(reporter)

    for reported, reporters in reported_dict.items():
        if len(reporters) >= k:
            stopped.append(reported)

    for reporter, reported in reporter_dict.items():
        mail_dict[reporter] = 0
        for whom in reported:
            if whom in stopped:
                mail_dict[reporter] += 1

    for id in id_list:
        if id not in mail_dict:
            answer.append(0)
        else:
            answer.append(mail_dict[id])
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
               2))