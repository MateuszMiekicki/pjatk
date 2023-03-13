#include <vector>
#include <iostream>
#include <algorithm>
#include <chrono>
#include <random>
#include <unordered_set>

namespace
{
    using container = std::vector<int>;
    container generateOrderContainer(std::size_t size)
    {
        container container(size);
        std::generate(container.begin(), container.end(), [n = 0]() mutable
                      { return n++; });
        return container;
    }
    container generateRandomContainer(std::size_t size)
    {
        std::mt19937 random{std::random_device{}()};
        std::unordered_set<int> selected;
        // note: upper bound may have a size problem because int is more small than size_t
        std::uniform_int_distribution dis(0, static_cast<int>(size * 10));
        while (selected.size() < size)
            selected.insert(dis(random));
        return container(selected.begin(), selected.end());
    }
    void sort(container &vec)
    {
        for (auto j{1}; j < vec.size(); ++j)
        {
            auto key = vec[j];
            int i = j - 1;
            while (i > -1 and vec[i] > key)
            {
                vec[i + 1] = vec[i];
                i--;
            }
            vec[i + 1] = key;
        }
    }
    std::chrono::nanoseconds benchmark(const container &vec)
    {
        auto vecCopy = vec;
        const auto start = std::chrono::high_resolution_clock::now();
        sort(vecCopy);
        const auto stop = std::chrono::high_resolution_clock::now();
        return std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    }
}

int main()
{
    // note: na potrzeby otrzymania wyników różnych od zera, zwiększyłem ilość elementów o rząd wielkości
    const auto amountOfElements = {2'000, 4'000, 16'000, 32'000, 20'000, 40'000, 160'000, 320'000};
    auto orderedCases = std::vector<container>(amountOfElements.size());
    auto randomCases = std::vector<container>(amountOfElements.size());
    std::transform(amountOfElements.begin(), amountOfElements.end(), orderedCases.begin(), generateOrderContainer);
    std::transform(amountOfElements.begin(), amountOfElements.end(), randomCases.begin(), generateRandomContainer);
    const auto amountOfCases = orderedCases.size();
    for (auto i{0}; i < amountOfCases; ++i)
    {
        std::cout << "for " << orderedCases[i].size() << " elements:\n";
        std::cout << "Order case: " << benchmark(orderedCases[0]).count() / static_cast<double>(orderedCases[i].size()) << "\n";
        std::cout << "Random case: " << benchmark(randomCases[0]).count() / static_cast<double>(randomCases[i].size()) << "\n";
    }
}