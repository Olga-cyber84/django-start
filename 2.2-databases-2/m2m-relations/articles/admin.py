from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Article, Scope
from django.core.exceptions import ValidationError
from pprint import pprint


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags = []
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            pprint(form.cleaned_data)
            data = form.cleaned_data
            for key in data:
                if key == 'is_main':
                    main_tags.append(form.cleaned_data[key])
        # вызовом исключения ValidationError можно указать админке о наличие ошибки
        # таким образом объект не будет сохранен,
        # а пользователю выведется соответствующее сообщение об ошибке
        if main_tags.count(True) == 0:
            print("ADD 1 MAIN TAG")
            raise ValidationError(
                'Укажите основной раздел')
        if main_tags.count(True) > 1:
            print("TOO MANY TAGS")
            raise ValidationError(
                'Основным может быть только один раздел')
        return super().clean()
        # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    # model = Article
    list_display = ['title', 'published_at']
