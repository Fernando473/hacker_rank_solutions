import unittest

from check_valid_project.solution import check_valid_project, clean_xlsx


class TestVerifyProjectName(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(check_valid_project('PIS-14-34 LABOMERSA S.A'), "PIS-14-34")

    def test_string_with_only_letters(self):
        self.assertEqual(check_valid_project('PIJ 15-09-REGULACION IVA-HUGO RUEDA REPRESENTAC'), "PIJ-15-09")

    def test_string_with_only_digits(self):
        self.assertEqual(check_valid_project("PIS-14-15-CÉSAR VÁSCONEZ-PAGO CALIBRACION Y CAM"), "PIS-14-15")

    def test_string_with_letters_followed_by_digits(self):
        self.assertEqual(check_valid_project('PIMI 14-04-VILLACRES JUAN FERNANDO-CONTRATO CIV'), "PIMI-14-04")

    def test_string_with_digits_followed_by_letters(self):
        self.assertEqual(check_valid_project('PIS-14-34-LABOMERSA S.A'), "PIS-14-34")

    def test_string_with_digits_followed_by_letters_and_digits(self):
        self.assertEqual(check_valid_project('PIMI15-12 VILLALBA MALDONADO SASKYA KARINA-PAGO'), "PIM-15-12")

    def test_string_with_digits_followed_by_letters_and_digits_and_letters(self):
        self.assertEqual(check_valid_project('PVS-2016-002 EMPAQUES ECUATORIANOS ECUAEMPAQUES'), "PVS-2016-002")

    def test_string_with_digits_followed_by_letters_and_digits_and_letters_and_digits(self):
        self.assertEqual(check_valid_project('PIJ 15-14-TECNOLOGIA INTERNACIONAL PARA EL ECUA'), "PIJ-15-14")

    def test_string_with_digits_followed_by_letters_and_digits_and_letters_and_digits_and_letters(self):
        self.assertEqual(check_valid_project('PROYECTO PIMI-14-16,BUISAR CIA LTDA, CONTRATO 2'), "PIMI-14-16")

    def test_string_with_digits_followed_by_letters_and_digits_and_letters_and_digits_and_letters_and_digits(self):
        self.assertEqual(check_valid_project('PROY PIMI-14-18, JOSE JALIL  HIJOS, POR ADQUISI'), "PIMI-14-18")

    def test_string_with_digits_followed_by_letters_and_digits_and_letters_and_digits_and_letters_and_digits_and_letters(
            self):
        self.assertEqual(check_valid_project('LIAVMS'), "LIAVMS")

    def test_string_with_digits_followed_by_letters_and_digits_and_letters_and_digits_and_letters_and_digits_and_letters_and_digits(
            self):
        self.assertEqual(check_valid_project('Rendición de la Entidad:177-4-0 No de fondo: 20'),
                         "Rendición de la Entidad:177-4-0 No de fondo: 20")

    def test_string_n2(self):
        self.assertEqual(check_valid_project('FONDO 20'), "FONDO 20")

    def test_string_n3(self):
        self.assertEqual(check_valid_project('Fondo: 13'), "Fondo: 13")

    def test_string_n4(self):
        self.assertEqual(check_valid_project('COMISIONES BANCARIAS'), "COMISIONES BANCARIAS")

    def test_string_n5(self):
        self.assertEqual(check_valid_project('REGISTRO DE GASTOS POR COMISIONES BANCARIAS, E'), "REGISTRO DE GASTOS POR COMISIONES BANCARIAS, E")

    def test_string_n6(self):
        self.assertEqual(check_valid_project('PII-DESODEH-006-2015'), "PII-DESODEH-006-2015")

class TestClean(unittest.TestCase):
    def test_n1(self):
        self.assertEqual(clean_xlsx('Rendición de la Entidad:177-4-0 No de fondo: 20'), "fondo:20")

    def test_n2(self):
        self.assertEqual(clean_xlsx('Rendición de la Entidad:177-4-0 No de fondo: 1'), "fondo:1")
if __name__ == '__main__':
    unittest.main()
