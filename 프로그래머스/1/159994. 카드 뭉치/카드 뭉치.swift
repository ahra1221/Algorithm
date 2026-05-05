import Foundation

func solution(_ cards1:[String], _ cards2:[String], _ goal:[String]) -> String {
    
    var head1 = 0
    var head2 = 0
    
    for g in goal {
        if head1 < cards1.count && cards1[head1] == g {
            head1 += 1
        } else if head2 < cards2.count && cards2[head2] == g {
            head2 += 1
        } else {
            return "No"
        }
    }
    
    return "Yes"
}