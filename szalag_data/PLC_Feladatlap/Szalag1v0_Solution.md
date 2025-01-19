# Szalag1v0
## _Üzemkezelés_
$ UzemF(SET) = Start \cdot \overline{Stop} \cdot \overline{Hiba1F} \cdot \overline{Hiba2F} $ <br>
$ UzemF(RESET) = Stop + Hiba1F + Hiba2F $

## _Működtetés_
$ M1 = TOF(UzemF) $ <br>
$ M1\_TOF(RT) = Hiba1F + Hiba2F $

$ Uzem = UzemF + \overline{UzemF} \cdot M2 \cdot Clock\_1Hz $

$ M2 = TOF(M1) $ <br>
$ M2\_TOF(RT) = Hiba2F $

## _Hibakezelés_
$ Hiba1F(SET) = TON(M1 \cdot \overline{S1}) $ <br>
$ Hiba1F(RESET) = Nyugta $

$ Hiba2F(SR) = TON(M2 \cdot \overline{S2}) $ <br>
$ Hiba2F(RESET) = Nyugta $
