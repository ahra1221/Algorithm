let X = Int(readLine()!)!

var sticks = [64]
var total = 64

while total > X {
    sticks.sort()

    let small = sticks.removeFirst()
    let half = small / 2
    sticks.append(half)
    total = total - small + half
    if total < X {
        sticks.append(half)
        total += half
    }
}
print(sticks.count)