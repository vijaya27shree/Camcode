//code for lcs should work
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int lcs(const string& s1, const string& s2) {
    int m = s1.length();
    int n = s2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    return dp[m][n];
}

vector<string> splitIntoWords(const string& str) {
    vector<string> words;
    stringstream ss(str);
    string word;
    while (ss >> word) {
        words.push_back(word);
    }
    return words;
}

vector<string> findSuggestions(const string& word, const vector<string>& wordList) {
    vector<string> suggestions;
    for (const string& w : wordList) {
        if (word != w && lcs(word, w) * 2 > word.length() && word.length() > 2) {
            suggestions.push_back(w);
        }
    }
    return suggestions;
}

int main() {
    // Read word and word list string from input
    string word, wordListStr;
    getline(cin, word);
    getline(cin, wordListStr);

    // Remove leading and trailing whitespaces from word
    word.erase(0, word.find_first_not_of(' '));
    word.erase(word.find_last_not_of(' ') + 1);

    // Remove leading and trailing whitespaces from wordListStr
    wordListStr.erase(0, wordListStr.find_first_not_of(' '));
    wordListStr.erase(wordListStr.find_last_not_of(' ') + 1);

    // Split word list string into individual words
    vector<string> wordVec = splitIntoWords(word);
    vector<string> wordList = splitIntoWords(wordListStr);

    // Find and print suggestions for each word in wordVec
    for (const string& w : wordVec) {
        vector<string> suggestions = findSuggestions(w, wordList);
        cout << "Suggestions for \"" << w << "\": ";
        for (const string& sug : suggestions) {
            cout << sug << ", ";
        }
        cout << endl;
    }

    return 0;
}

// levenstein algo
// #include <iostream>
// #include <string>
// #include <vector>
// #include <sstream>
// #include <algorithm>

// using namespace std;

// int levenshteinDistance(const string& word1, const string& word2) {
//     int m = word1.length();
//     int n = word2.length();

//     vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

//     for (int i = 0; i <= m; ++i)
//         dp[i][0] = i;

//     for (int j = 0; j <= n; ++j)
//         dp[0][j] = j;

//     for (int i = 1; i <= m; ++i) {
//         for (int j = 1; j <= n; ++j) {
//             if (word1[i - 1] == word2[j - 1])
//                 dp[i][j] = dp[i - 1][j - 1];
//             else
//                 dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
//         }
//     }

//     return dp[m][n];
// }

// vector<string> splitIntoWords(const string& str) {
//     vector<string> words;
//     stringstream ss(str);
//     string word;
//     while (ss >> word) {
//         words.push_back(word);
//     }
//     return words;
// }

// vector<string> findSuggestions(const string& word, const vector<string>& wordList) {
//     vector<string> suggestions;
//     for (const string& w : wordList) {
//         if (levenshteinDistance(word, w) <= 2)
//             suggestions.push_back(w);
//     }
//     return suggestions;
// }

// int main() {
//     // Read word and word list string from input
//     string word, wordListStr;
//     getline(cin, word);
//     getline(cin, wordListStr);

//     // Remove leading and trailing whitespaces from word
//     word.erase(0, word.find_first_not_of(' '));
//     word.erase(word.find_last_not_of(' ') + 1);

//     // Remove leading and trailing whitespaces from wordListStr
//     wordListStr.erase(0, wordListStr.find_first_not_of(' '));
//     wordListStr.erase(wordListStr.find_last_not_of(' ') + 1);

//     // Split word list string into individual words
//     vector<string> wordVec = splitIntoWords(word);
//     vector<string> wordList = splitIntoWords(wordListStr);

//     // Find and print suggestions for each word in wordVec
//     for (const string& w : wordVec) {
//         vector<string> suggestions = findSuggestions(w, wordList);
//         cout << "Suggestions for \"" << w << "\": ";
//         for (const string& sug : suggestions) {
//             cout << sug << ", ";
//         }
//         cout << endl;
//     }

//     return 0;
// }
//levenstein2
// #include <iostream>
// #include <string>
// #include <vector>
// #include <sstream>
// #include <algorithm>

// using namespace std;

// int levenshteinDistance(const string& word1, const string& word2) {
//     int m = word1.length();
//     int n = word2.length();

//     vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

//     for (int i = 0; i <= m; ++i)
//         dp[i][0] = i;

//     for (int j = 0; j <= n; ++j)
//         dp[0][j] = j;

//     for (int i = 1; i <= m; ++i) {
//         for (int j = 1; j <= n; ++j) {
//             if (word1[i - 1] == word2[j - 1])
//                 dp[i][j] = dp[i - 1][j - 1];
//             else
//                 dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
//         }
//     }

//     return dp[m][n];
// }

// vector<string> splitIntoWords(const string& str) {
//     vector<string> words;
//     stringstream ss(str);
//     string word;
//     while (ss >> word) {
//         words.push_back(word);
//     }
//     return words;
// }

// vector<string> findSuggestions(const string& word, const vector<string>& wordList) {
//     vector<string> suggestions;
//     for (const string& w : wordList) {
//         if (levenshteinDistance(word, w) <= 2) // Adjust the threshold here
//             suggestions.push_back(w);
//     }
//     return suggestions;
// }

// int main() {
//     // Read word and word list string from input
//     string word, wordListStr;
//     getline(cin, word);
//     getline(cin, wordListStr);

//     // Remove leading and trailing whitespaces from word
//     word.erase(0, word.find_first_not_of(' '));
//     word.erase(word.find_last_not_of(' ') + 1);

//     // Remove leading and trailing whitespaces from wordListStr
//     wordListStr.erase(0, wordListStr.find_first_not_of(' '));
//     wordListStr.erase(wordListStr.find_last_not_of(' ') + 1);

//     // Split word list string into individual words
//     vector<string> wordVec = splitIntoWords(word);
//     vector<string> wordList = splitIntoWords(wordListStr);

//     // Find and print suggestions for each word in wordVec
//     for (const string& w : wordVec) {
//         vector<string> suggestions = findSuggestions(w, wordList);
//         cout << "Suggestions for \"" << w << "\": ";
//         for (const string& sug : suggestions) {
//             cout << sug << ", ";
//         }
//         cout << endl;
//     }

//     return 0;
// }




