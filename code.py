# 1. Basic Python Concepts

"""Reverse a String Write a Python function to reverse a string."""
def reverse_string(s:str) -> str:
    return s[::-1]

""" Check for Palindrome Determine if a string is a palindrome""".
def is_palindrone(s: str) -> str:
    return s == s[::-1]

#-------------------------------------------------
# 2. Text Similarity Using Cosine Similarity
from collections import Counter
import math

def compute_cosine_similarity(str1, str2):
    # Tokenize strings into words
    words1 = str1.lower().split()
    words2 = str2.lower().split()
    
    # Count word frequencies
    freq1 = Counter(words1)
    freq2 = Counter(words2)
    
    # Get the unique words
    unique_words = set(freq1.keys()).union(set(freq2.keys()))
    
    # Create vectors
    vec1 = [freq1[word] for word in unique_words]
    vec2 = [freq2[word] for word in unique_words]
    
    # Compute dot product and magnitudes
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(v ** 2 for v in vec1))
    magnitude2 = math.sqrt(sum(v ** 2 for v in vec2))
    
    # Compute cosine similarity
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    
    cosine_similarity = dot_product / (magnitude1 * magnitude2)
    return round(cosine_similarity, 3)

# Example usage
str1 = "TikTok is a popular platform"
str2 = "TikTok platform is gaining popularity"
print("Cosine Similarity:", compute_cosine_similarity(str1, str2))
# -------------------------------------------------

# Optimzied
from collections import Counter
import math

def compute_cosine_similarity(str1, str2):
    # Tokenize and count word frequencies
    freq1 = Counter(str1.lower().split())
    freq2 = Counter(str2.lower().split())
    
    # Compute dot product directly
    dot_product = sum(freq1[word] * freq2[word] for word in freq1.keys() & freq2.keys())
    
    # Compute magnitudes directly
    magnitude1 = math.sqrt(sum(v ** 2 for v in freq1.values()))
    magnitude2 = math.sqrt(sum(v ** 2 for v in freq2.values()))
    
    # Avoid division by zero
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    
    # Compute cosine similarity
    cosine_similarity = dot_product / (magnitude1 * magnitude2)
    return round(cosine_similarity, 3)

# Example usage
str1 = "TikTok is a popular platform"
str2 = "TikTok platform is gaining popularity"
print("Cosine Similarity:", compute_cosine_similarity(str1, str2))
# -------------------------------------------------
