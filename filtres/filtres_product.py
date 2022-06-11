from telebot import AdvancedCustomFilter, types
from telebot.callback_data import CallbackData, CallbackDataFilter


products_factory = CallbackData('product_id', prefix='products')

productbay_basked = CallbackData('productbay_id', prefix='product')



class ProductsCallbackFilter(AdvancedCustomFilter):
    key ="config"
    def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)

