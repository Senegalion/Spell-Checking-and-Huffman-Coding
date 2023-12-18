def levenshteinDistance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]


def hammingDistance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must have equal length for Hamming distance calculation.")

    return sum(el1 != el2 for el1, el2 in zip(s1, s2))


def inDelDistance(string_a, string_b):
    m = len(string_a)
    n = len(string_b)

    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string_a[i - 1] == string_b[j - 1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    return matrix[m][n]


def modLevenshteinDistance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    substitutionWeights = {
        ('o', 'p'): 0.5,
    }

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                substitutionWeight = substitutionWeights.get((s1[i - 1], s2[j - 1]), 1.0)
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + substitutionWeight
                )

    return dp[m][n]


def modHammingDistance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must have equal length for Hamming distance calculation.")

    weights = {
        ('o', 'p'): 0.5,
        ('i', 'l'): 0.5,
        ('n', 'm'): 0.5,
    }

    return sum(
        weights.get((ch1, ch2), 1.0)
        if ch1 != ch2
        else 0
        for ch1, ch2 in zip(s1, s2)
    )


def Correct(incorrect_word):
    dictionaryFile = "words_alpha.txt"
    minDistance = float('inf')
    suggestedWord = None

    with open(dictionaryFile, "r") as file:
        for word in file:
            word = word.strip()
            distance = modLevenshteinDistance(incorrect_word, word)

            if distance < minDistance:
                minDistance = distance
                suggestedWord = word

    return suggestedWord


def correctFile(input_file, output_file):
    with open(input_file, "r") as input_file, open(output_file, "w") as output_file:
        for line in input_file:
            correctedLine = ""
            words = line.strip().split()

            for word in words:
                if word.isalpha():
                    corrected_word = Correct(word.lower())
                    correctedLine += corrected_word + " "
                else:
                    correctedLine += word + " "

            output_file.write(correctedLine.strip() + "\n")


# Example usage
correctFile("input.txt", "output.txt")

string1 = "Algambra"
string2 = "Alahmaba"

Levenstein = modLevenshteinDistance(string1, string2)
print("Modified Levenshtein Distance between "+string1+" & "+string2+" is " + str(Levenstein))

Hamming = modHammingDistance(string1, string2)
print(f"Modified Hamming distance between '{string1}' and '{string2}': {Hamming}")

indelDistance = inDelDistance(string1, string2)
print(f"Indel distance between '{string1}' and '{string2}': {indelDistance}")