"""
Paragraph Structure & Content Readability Optimizer
Part of SyntaxCraft SEO & Webmaster Automation Utilities.
Computes Flesch-Kincaid readability and optimizes paragraph distribution.
"""

import re
from typing import Dict, Any, List

def count_syllables(word: str) -> int:
    word = word.lower().strip()
    if len(word) <= 3:
        return 1
    word = re.sub(r'(?:[^laeiouy]|ed|es|e)$', '', word)
    word = re.sub(r'^y', '', word)
    syllables = len(re.findall(r'[aeiouy]{1,2}', word))
    return max(1, syllables)

def audit_readability(text: str) -> Dict[str, Any]:
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    words = [w.strip() for w in re.split(r'\s+', re.sub(r'[^\w\s]', '', text)) if w.strip()]
    
    total_sentences = max(1, len(sentences))
    total_words = max(1, len(words))
    total_syllables = sum(count_syllables(w) for w in words)
    
    # Standard Flesch Reading Ease Formula
    score = 206.835 - (1.015 * (total_words / total_sentences)) - (84.6 * (total_syllables / total_words))
    score = max(0.0, min(100.0, round(score, 1)))
    
    # Grade level
    grade_level = (0.39 * (total_words / total_sentences)) + (11.8 * (total_syllables / total_words)) - 15.59
    grade_level = max(1.0, round(grade_level, 1))

    return {
        "flesch_reading_ease": score,
        "grade_level": grade_level,
        "total_words": total_words,
        "total_sentences": total_sentences,
        "avg_sentence_length": round(total_words / total_sentences, 1),
        "is_optimal": score >= 60.0
    }

def format_paragraphs(text: str, target_words_per_para: int = 45) -> List[str]:
    """
    Splits long monolithic text walls into readable, high-retention paragraphs.
    """
    sentences = [s.strip() + "." for s in re.split(r'[.!?]+', text) if s.strip()]
    paragraphs = []
    current_para = []
    current_words = 0
    
    for sentence in sentences:
        words_in_s = len(sentence.split())
        current_para.append(sentence)
        current_words += words_in_s
        
        if current_words >= target_words_per_para:
            paragraphs.append(" ".join(current_para))
            current_para = []
            current_words = 0
            
    if current_para:
        paragraphs.append(" ".join(current_para))
        
    return paragraphs

if __name__ == "__main__":
    sample = (
        "Modern digital business operations depend on concise communication and fast indexing. "
        "When visitors arrive on a product page they scan headings and bullet points rather than "
        "reading continuous walls of text. Clean paragraph structure and search intent optimization "
        "guarantee better engagement metrics and higher search rankings across competitive niches."
    )
    paras = format_paragraphs(sample, target_words_per_para=25)
    stats = audit_readability(sample)
    print("✓ Paragraphs formed:", len(paras))
    print("✓ Readability Stats:", stats)
