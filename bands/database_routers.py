class SakilaRouter:
    """
    Router to control all database operations on models in the Sakila application
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'sakila':
            return 'sakila'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'sakila':
            return 'sakila'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'sakila' or obj2._meta.app_label == 'sakila':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'sakila':
            return db == 'sakila'
        return None