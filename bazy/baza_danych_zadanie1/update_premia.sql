UPDATE "pracownicy" SET "pracownicy"."premia" = "pracownicy"."pensja zasadnicza" * (select "premia"."premia" FROM "premia" WHERE "pracownicy"."stanowisko" = "premia"."stanowisko");
