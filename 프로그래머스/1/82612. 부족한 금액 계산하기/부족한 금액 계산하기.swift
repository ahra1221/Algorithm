import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    let money = Int64(money)
    var pay: Int64 = 0
    for i in 1...count {
        pay += Int64(price * i)
    }
    return pay > money ? pay - money : Int64(0)
}