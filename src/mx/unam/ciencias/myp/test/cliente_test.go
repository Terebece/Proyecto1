package cliente

import "testing"

func TestGetSaludo(t *testing.T)  {
	message := getSaludo()
	if message != "Hola"{
		t.Error("Se esperaba 'Hola' y se obtuvo", message)
	}
}
