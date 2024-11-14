#include <cs50.h>
#include <stdio.h>
#include <strings.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for(int i = 0; i < candidate_count; i++)
    {
        if(strcasecmp(name, candidates[i]) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

void initialize_prefences(void)
{
    for(int i = 0; i < candidate_count; i++)
    {
        for(int j = 0; j < candidate_count; j++)
            preferences[i][j] = 0;
    }

    return;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for(int i = 0; i < candidate_count -1; i++)
    {
        for(int j = 1 + i; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }

    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    int k = 0;
    for(int i = 0; i < candidate_count - 1; i++)
    {
        for(int j = 1 + i; j < candidate_count; j++)
        {
            if(preferences[i][j] > preferences[j][i])
            {
                pairs[k].winner = i;
                pairs[k].loser = j;
                k++;
            }

            if(preferences[i][j] < preferences[j][i])
            {
                pairs[k].winner = j;
                pairs[k].loser = i;
                k++;
            }
        }
    }

    pair_count = k;

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    int temp[pair_count];
    int temp_winner;
    int temp_loser;
    int t;

    for(int i = 0; i < pair_count; i++)
        temp[i] = preferences[pairs[i].winner][pairs[i].loser] - preferences[pairs[i].loser][pairs[i].winner];

    for(int i = 0; i < pair_count; i++)
    {
        for(int j = 1 + i; j < pair_count - 1; j++)
        {
            if(temp[i] < temp[j])
            {
                temp_winner = pairs[i].winner;
                pairs[i].winner = pairs[j].winner;
                pairs[j].winner = temp_winner;

                temp_loser = pairs[i].loser;
                pairs[i].loser = pairs[j].loser;
                pairs[j].loser = temp_loser;

                t = temp[i];
                temp[i] = temp[j];
                temp[j] = t;
            }
        }
    }

    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    bool is_cycle;

    for(int i = 0; i < pair_count; i++)
    {
        is_cycle = true;

        locked[pairs[i].winner][pairs[i].loser] = true;

        for (int j = 0; j < candidate_count; j++)
        {
            if(!locked[j][(j + 1) % candidate_count])
                is_cycle = false;
        }

        if(is_cycle)
            locked[pairs[i].winner][pairs[i].loser] = false;
    }

    return;
}

// Print the winner of the election
void print_winner(void)
{
    bool is_source;
    int index;

    for (int i = 0; i < candidate_count; i++)
    {
        is_source = true;
        index = i;

        for (int j = 0; j < candidate_count; j++)
        {
            if(locked[j][i])
            {
                is_source = false;
                break;
            }
        }
        if(is_source)
            break;
    }

    printf("%s\n",candidates[index]);

    return;
}
