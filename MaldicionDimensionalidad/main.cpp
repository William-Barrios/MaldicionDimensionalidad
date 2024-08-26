//
//  main.cpp
//  MaldicionDimensionalidad
//
//  Created by William Alexis Barrios Concha on 22/08/24.
//

#include <iostream>
#include <cmath>
#include <vector>
#include <random>
#include <fstream>
using namespace std;

void process(vector<vector<double>>& tocalc, int dimension){
    
    random_device rd;  // Will be used to obtain a seed for the random number engine
    mt19937 gen(rd()); // Standard mersenne_twister_engine seeded with rd()
    uniform_real_distribution<> dis(1.0, 2.0);
    for(int i=0;i<100;i++){
        vector<double>temp;
        for (int n = 0; n < dimension; ++n)
            temp.push_back(dis(gen));
        tocalc.push_back(temp);
    }
}

void functDistancia(vector<vector<double>>& tocalc, const string& filename){
    ofstream file(filename); // Open file for writing
        if (!file.is_open()) {
            cerr << "Error opening file!" << endl;
            return;
        }
    int dim = tocalc[0].size();
    int canPuntos = tocalc.size();
    int cantDist =0;
    for(int i = 0;i<canPuntos;i++){
        for(int o=i+1;o<canPuntos;o++){
            double sum=0;
            for(int j =0; j<dim;j++)
                sum+=pow(tocalc[o][j]-tocalc[i][j],2);
            sum=sqrt(sum);
            file << sum << endl;
            cantDist++;
        }
    }
    file.close();
    cout<<cantDist;
}

int main(int argc, const char * argv[]) {
    
    vector<vector<double>>vect10;
    vector<vector<double>>vect50;
    vector<vector<double>>vect100;
    vector<vector<double>>vect500;
    vector<vector<double>>vect1000;
    vector<vector<double>>vect2000;
    vector<vector<double>>vect5000;
    process(vect10, 10);
    process(vect50, 50);
    process(vect100, 100);
    process(vect500, 500);
    process(vect1000, 1000);
    process(vect2000, 2000);
    process(vect5000, 5000);
    functDistancia(vect10, "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect10.txt");
    functDistancia(vect50, "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect50.txt");
    functDistancia(vect100, "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect100.txt");
    functDistancia(vect500, "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect500.txt");
    functDistancia(vect1000, "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect1000.txt");
    functDistancia(vect2000, "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect2000.txt");
    functDistancia(vect5000, "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect5000.txt");
    
    
    
    
    return 0;
}
