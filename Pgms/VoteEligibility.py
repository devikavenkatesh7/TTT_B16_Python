
def voteEligibility(age):
    if(age>18):
        eligible="Candidate is eligible to vote"
    else:
        eligible="Candidate should have age above 18 to vote"
    return eligible


vote=(voteEligibility(13))
print(vote)

