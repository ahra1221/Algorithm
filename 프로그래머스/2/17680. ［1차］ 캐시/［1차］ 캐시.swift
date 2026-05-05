func solution(_ cacheSize:Int, _ cities:[String]) -> Int {
    
    if cacheSize == 0 {
        return cities.count * 5
    }
    
    var cache: [String:Int] = [:]
    var time = 0
    for (idx, c) in cities.enumerated() {
        let city = c.lowercased()
        if let _ = cache[city] {
            cache[city] = idx
            time += 1
        } else {
            if cache.count >= cacheSize {
                let deleteKey = cache.min { $0.value < $1.value }!.key
                cache[deleteKey] = nil
            }
            cache[city] = idx
            time += 5
        }
    }
    return time
}