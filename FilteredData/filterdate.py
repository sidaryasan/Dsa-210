#include <iostream>
#include <fstream>
#include <string>

// Belirli aralıkta mı diye kontrol
bool isDateInRange(const std::string& line) {
    size_t pos = line.find("startDate=\"");
    if (pos == std::string::npos) return false;

    std::string dateStr = line.substr(pos + 11, 10); // "2024-09-01" gibi

    return (dateStr >= "2024-09-01" && dateStr <= "2025-04-23");
}

int main() {
    std::ifstream inputFile("output.txt");
    std::ofstream outputFile("filtered_by_date.txt");

    if (!inputFile.is_open() || !outputFile.is_open()) {
        std::cerr << "Dosyalar açılamadı!" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(inputFile, line)) {
        if (isDateInRange(line)) {
            outputFile << line << std::endl;
        }
    }

    inputFile.close();
    outputFile.close();

    std::cout << "Filtreleme tamamlandı. Çıktı dosyası: filtered_by_date.txt" << std::endl;

    return 0;
}
