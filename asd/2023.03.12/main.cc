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
    void sort(std::vector<int> &vec)
    {
        for (int j{1}; j < vec.size(); ++j)
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
}

int main()
{
    const auto size = 1'000'000;
    {
        auto vec = generateRandomContainer(size);
        const auto start = std::chrono::high_resolution_clock::now();
        sort(vec);
        const auto stop = std::chrono::high_resolution_clock::now();
        std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(stop - start).count() / static_cast<double>(size) << "\n";
    }
    {
        auto vec = generateOrderContainer(size);
        const auto start = std::chrono::high_resolution_clock::now();
        sort(vec);
        const auto stop = std::chrono::high_resolution_clock::now();
        std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(stop - start).count() / static_cast<double>(size) << "\n";
    }
}