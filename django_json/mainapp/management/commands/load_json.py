import json
from django.core.management import BaseCommand, CommandError
from mainapp.models import Dictionary, Product, Order


class Command(BaseCommand):
    help = 'Parse json into db'

    file_keys = {
        "DICT": "mainapp/fixtures/dict.json",
        "PROD": "mainapp/fixtures/data_1.json",
        "ORD": "mainapp/fixtures/data_2.json",
    }

    # todo сделать добавление агрумента с указанием имени файла (так как файлы разные не факт
    #  что получится сделать под каждый json  общую структуру
    def add_arguments(self, parser):
        # add data to Dictionary
        parser.add_argument(
            '--dict',
            action='store_true',
            default=False,
            help='Load Dictionary from json'
        )
        # add data to Product
        parser.add_argument(
            '--product',
            action='store_true',
            default=False,
            help='Load Product from json'
        )
        # add data to Order
        parser.add_argument(
            '--order',
            action='store_true',
            default=False,
            help='Load Order from json'
        )

    def handle(self, *args, **options):

        if options['dict']:
            self.parse_dict()
        elif options['product']:
            self.parse_product()
        elif options['order']:
            self.parse_order()

    def parse_order(self):
        # todo сделать обработчик времени
        with open(self.file_keys['ORD'], "r", encoding="utf-8") as read_file:
            data = json.loads(read_file.read())
            dict_data = {}
            for el in data:
                r_n_u_m = el['R_N_U_M']
                indicators = el['DIM_2954']
                view_type = el['DIM_369']
                is_calc = el['IS_CALC']
                country = el['DIM_2927']
                direction_of_travel = el['DIM_2955']
                goods_apk = el['DIM_2956']
                goods_industrial = el['DIM_2957']
                type_of_goods_industrial = el['DIM_2958']
                type_of_goods_apk = el['DIM_2959']
                ddate = el['DDATE']
                # dt = el['DT']
                dl = el['DL']
                id_ind = el['ID_IND']
                vl = el['VL']
                dict_data = {
                    'r_n_u_m': r_n_u_m,
                    'indicators': indicators,
                    'view_type': view_type,
                    'is_calc': is_calc,
                    'country': country,
                    'direction_of_travel': direction_of_travel,
                    'goods_apk': goods_apk,
                    'type_of_goods_industrial': type_of_goods_industrial,
                    'ddate': ddate,
                    # 'dt': dt,
                    'dl': dl,
                    'id_ind': id_ind,
                    'vl': vl,
                }
                try:
                    # dic = Dictionary.objects.get_or_create(ident=goods_apk)
                    prod = Product.objects.get(n_order=type_of_goods_apk)
                    order = Order.objects.create(**dict_data, type_of_goods_apk=prod)
                    print(f'{order}')
                except Order.DoesNotExist:
                    raise CommandError('Error')
                self.stdout.write(self.style.SUCCESS(f'Successfully added instance {type_of_goods_industrial}'))

    def parse_product(self):
        # todo подумать как сделать один метод для парсинга product и dictionary
        with open(self.file_keys['PROD'], "r", encoding="utf-8") as read_file:
            data = json.loads(read_file.read())
            dict_data = {}
            for el in data:
                ids = el['id']
                parent_id = el['parent_id']
                name = el['name']
                n_order = el['n_order']
                methodology = el['methodology']
                ei = el['ei']
                dict_data = {
                    'ids': ids,
                    'parent_id': parent_id,
                    'name': name,
                    'n_order': n_order,
                    'methodology': methodology,
                    'ei': ei
                }
                try:
                    product = Product.objects.create(**dict_data)
                except Product.DoesNotExist:
                    raise CommandError('Error')
                product.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully added instance {name}'))

    def parse_dict(self):
        # открываю файл
        with open(self.file_keys['DICT'], "r", encoding="utf-8") as read_file:
            # разбираю json
            data = json.loads(read_file.read())
            dict_data = {}
            for el in data:
                ids = el['id']
                dim_name = el['dim_name']
                ident = el['ident']
                is_ind = el['is_ind']
                dict_data = {
                    'ids': ids,
                    'dim_name': dim_name,
                    'ident': ident,
                    'is_ind': is_ind
                }
                try:
                    # указанные поля из json передаю в поля класса и создаю объекты в базе данных
                    dict = Dictionary.objects.create(**dict_data)
                except Dictionary.DoesNotExist:
                    raise CommandError('Error')
                dict.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully added instance {dim_name}'))
