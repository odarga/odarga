#include <cs50.h>
#include <math.h>
#include <stdio.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

double calculate_index(int letters, int words, int sentences);



int main(void)
{
    int letters;
    int words;
    int sentences;
    int index;

    string text = get_string("Text: ");

    letters = count_letters(text);                                  // Counting letters
    words = count_words(text);                                      // Counting words
    sentences = count_sentences(text);                              // Counting sentences

    index = calculate_index(letters, words, sentences);             // Calculating index

    if(index < 1)
        printf("Before Grade 1\n");
    else if (index >= 16)
        printf("Grade 16+\n");
    else
        printf("Grade %d\n",index);
}



// Counting letters
int count_letters(string text)
{
    int i = 0;
    int letters =0;

    while(text[i] != '\0')
    {
        if((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
            letters++;
        i++;
    }

    return letters;
}

// Counting words
int count_words(string text)
{
    int i = 0;
    int words =0;

    while(text[i] != '\0')
    {
        if(text[i] == ' ')
            words++;
        i++;
    }

    return words+1;
}

// Counting sentences
int count_sentences(string text)
{
    int i = 0;
    int sentences =0;

    while(text[i] != '\0')
    {
        if(text[i] == '.' || text[i] == '!' || text[i] == '?')
            sentences++;
        i++;

    }

    return sentences;
}

// Coleman-Liau index
double calculate_index(int letters, int words, int sentences)
{
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;

    return round(((0.0588 * L) - (0.296 * S) - 15.8));
}
