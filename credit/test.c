unsigned int improved_hash(const char *word)
{
    unsigned int hash = 0;
    while (*word)
    {
        hash = (hash << 2) ^ toupper(*word++);
    }
    return hash % N;
}
