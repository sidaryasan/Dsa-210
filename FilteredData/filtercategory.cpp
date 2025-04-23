#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <filesystem>

std::string extractType(const std::string& line) {
    size_t start = line.find("type=\"");
    if (start == std::string::npos) return "";

    start += 6; // "type=\"" sonrası
    size_t end = line.find("\"", start);
    if (end == std::string::npos) return "";

    return line.substr(start, end - start);
}

int main() {
    std::ifstream inputFile("filtered_by_date.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Girdi dosyası açılamadı!" << std::endl;
        return 1;
    }

    std::unordered_map<std::string, std::ofstream> categoryFiles;
    std::string line;

    while (std::getline(inputFile, line)) {
        std::string type = extractType(line);
        if (type.empty()) continue;

        // Dosya yoksa oluştur
        if (categoryFiles.find(type) == categoryFiles.end()) {
            std::string fileName = type + ".txt";
            categoryFiles[type].open(fileName);
            if (!categoryFiles[type].is_open()) {
                std::cerr << "Dosya açılamadı: " << fileName << std::endl;
                continue;
            }
        }

        // Satırı yaz
        categoryFiles[type] << line << std::endl;
    }

    // Tüm dosyaları kapat
    for (auto& [_, file] : categoryFiles) {
        file.close();
    }

    inputFile.close();

    std::cout << "Tüm kayıtlar kategorilere göre ayrıldı." << std::endl;
    return 0;
}
