// Ya me estoy dando una idea de como es que funciona la microbiología :)

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double N0 = 0, r = 0, t = 0;
    double poblacion_final = 0;
    cout << "Ingrese la cantidad inicial de bacterias (N0): ";
    cin >> N0;
    cout << "Ingrese la tasa de crecimiento (r): ";
    cin >> r;
    cout << "Ingrese el tiempo transcurrido (t): ";
    cin >> t;

    // formula de crecimiento exponencial: N(t) = N0 * e^(rt)
    poblacion_final= N0 * exp(r * t);
    cout << "La cantidad de bacterias despues de " << t << " horas es: " << poblacion_final << endl;

    if (poblacion_final > (N0 * 2)) {
        cout << "La poblacion de bacterias se ha duplicado." << endl;
    } else {
        cout << "La poblacion de bacterias no se ha duplicado." << endl;
    }

    return 0;
}