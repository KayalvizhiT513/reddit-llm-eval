# reddit-llm-eval
# Reddit Personal Finance Q&A Evaluation Dataset

This repository contains a minimal, read-only research tool for collecting publicly available Reddit discussions related to personal finance.

## Purpose

The goal of this project is to support **offline evaluation of language models** used for financial education and general personal finance assistance.  
The tool collects question-and-answer style Reddit threads to analyze:
- Common financial literacy questions
- Reasoning patterns in community responses
- Answer completeness and clarity

This project is **research-oriented** and **non-interactive**.

## Scope and Limitations

The application:
- Uses Reddit’s official API via a standard library
- Accesses **only publicly available content**
- Operates in a **read-only** manner
- Does not post, comment, vote, message users, or moderate content
- Does not attempt to identify or profile Reddit users

Usernames and direct identifiers are removed before downstream processing.

## Subreddits

Examples of subreddits accessed:
- r/personalfinance
- r/FinancialPlanning
- r/IndiaInvestments

The tool respects subreddit rules and Reddit API rate limits.

## Data Usage

Collected content is used solely for:
- Model evaluation
- Quality benchmarking
- Research and experimentation

The data is not redistributed as a raw dataset and is not used to recreate Reddit experiences.

## Compliance

This project is designed to comply with:
- Reddit Responsible Builder Policy
- Reddit API Terms of Use

## Technology

- Python 3
- PRAW (Python Reddit API Wrapper)

## Disclaimer

This repository is provided for research and evaluation purposes only.  
It is not affiliated with or endorsed by Reddit.
