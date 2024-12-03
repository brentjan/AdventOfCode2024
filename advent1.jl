using DataStructures

number_regex = r"^(\d+)\s+(\d+)$"
result = 0
left = []
right = []

open("data/advent1.in") do file
    while !eof(file)
        line = readline(file)
        matches = match(number_regex, line)

        push!(left, parse(Int, matches[1]))
        push!(right, parse(Int, matches[2]))
    end
end

right_counter = counter(right)

for l in left
    global result += l * right_counter[l]
end

println(result)
