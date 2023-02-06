### Program pozwalający organizować grupowe wydatki, ułatwiający dzielenie się i śledzenie wydatków ze znajomymi.

Głównym zadaniem programu jest obliczenie za pomocą zachłannego algorytmu optymalnej liczby przelewów na podstawie podanych transakcji

#### Inne funkcjonalności:

W głównym menu użytkownik może:
* wyświetlić istniejące już grupy wydatków
* przejść do menu podanej grupy wydatków 
* dodać nową grupę wydatków

W menu grupy wydatków użytkownik może:
* wyświetlić osoby do niej należące
* dodać nową osobę
* wyświetlić transakcje 
* dodać transakcję
* usunąć transakcję
* pokazać bilans kosztów osób w grupie
* obliczyć optymalne przelewy (*)

(*) - dla bardziej skomplikowanych przypadków algorytm może zwrócić dobrą, lecz nie optymalną liczbę przelewów

#### Pojęcia:

W ramach grupy wydatków (expenses_group.py) definiowane są:
* nazwa grupy
* osoby do niej należące
* lista transakcji

W ramach transakcji (transaction.py) definiowane są:
* nazwa transakcji
* całkowity koszt
* osoby uczestniczące
* osoba opłacająca transakcję
* bilansy osób

W ramach przelewu (transfer.py) definiowane są:
* osoba otrzymująca przelew
* osoba wykonująca przelew
* suma przelewu