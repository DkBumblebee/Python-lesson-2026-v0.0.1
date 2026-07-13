# Create a list
names = ["Alice", "Bob", "Charlie", "John"]
scores = [85, 72, 91, 68, 67, 99]

print(names)
print(scores[2])
print(f"Names: {len(names)}, Scores: {len(scores)}")


names.append("Dave")
names.remove("Bob") 
print(names)
# Mean 
print(sum(scores) / len(scores))