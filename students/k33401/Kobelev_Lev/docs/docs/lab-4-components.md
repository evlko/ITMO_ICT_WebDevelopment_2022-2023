# Components

## Views

1. HomeView. Все сценарии.
2. ScenarioView. Конкретный сценарий.

## Layouts

1. CardsLayout. Используется в HomeView.
2. ScenarioLayout. Используется в ScenarioView.

## Components

1. HeaderMenu. Хедер, используется в App.
2. FooterMenu. Футер, используется в App.
3. LogInPopUp. Модальное окно входа, используется в App.
4. SignUpPopUp. Модальное окно регистрации, используется в App.
5. FilterMenu. Меню фильтрации, используется в HomeView.
6. FilterCheckbox. Чекбокс фильтрации, используется в FilterMenu.
7. OrderButton. Кнопка порядка сортировки, используется в FilterMenu.
8. SortingButton. Кнопка вида сортировки, используется в FilterMenu.
9. TagButton. Кнопка фильтрации по тегу, используется в FilterMenu.
10. ScenarioCard. Карточка сценария.
11. LikeButton. Кнопка лайка, используется в ScenarioCard.
12. TagCapsule. Капсула тэга, используется в ScenarioCard.
13. ReviewCard. Карточка отзыва, используется в ScenarioLayout.
14. ReviewForm. Карточка отзыва, используется в ScenarioLayout.
15. GameSystemButton. Кнопка (по факту всё же чек бокс) игровой системы, используется в FilterMenu.

# Пример связей

Во время работы по максимум использовались возможности вью. 

Рассмотрим на примере фильтрации и сортировки.

## FilterMenu

### scripts

``` javascript
export default {
    name: "FilterMenu",

    components: {SortingButton, GameSystemButton, TagButton, FilterCheckbox, OrderButton},

    data() {
        return {
            // опции для сортировки, то есть словарь параметров, которые далее отправятся в API
            options: {},
            // виды сортировки опредляются (и осуществляются) на фронта
            sortingOptions: [{
                name: 'Name',
                id: 'name'
            }, {
                name: 'Likes',
                id: 'likes'
            }, {
                name: 'Date',
                id: 'publish_date'
            }],
            flagOptions: [{
                name: 'Adult',
                id: 'adult'
            }, {
                name: 'Finished',
                id: 'finished'
            }],
            ascendingSorting: true,
            currentSortingKey: 'name',
        }
    },
    
    // получаем необходимые данные из сторов, чтобы создать нужные компоненты
    computed: {
        ...mapState(useGameSystemsStore, ['gameSystems']),
        ...mapState(useTagsStore, ['tags']),
    },
    
    // загружаем данные, фильтруем, сортируем
    methods: {
        ...mapActions(useGameSystemsStore, ['loadGameSystems']),
        ...mapActions(useTagsStore, ['loadTags']),
        ...mapActions(useScenariosStore, ['filterScenarios', 'sortScenarios']),
        SelectOption: function (value, key) {
            this.options[key] = this.options[key] || [];

            if (this.options[key].includes(value)) {
                const index = this.options[key].indexOf(value);
                this.options[key].splice(index, 1)
            } else {
                this.options[key].push(value)
            }
        },
        FilterScenarios: function () {
            this.filterScenarios(this.options).then(() => {
                this.SortScenarios()
            })
        },
        ChangeSortingKey: function(key) {
            this.currentSortingKey = key
            this.SortScenarios()
        },
        ChangeOrder: function (order) {
            this.ascendingSorting = order
            this.SortScenarios()
        },
        SortScenarios: function () {
            this.sortScenarios(this.currentSortingKey, this.ascendingSorting)
        },
    },

    mounted() {
        this.loadGameSystems()
        this.loadTags()
    }
}
```

### part of a template

циклом отрисовываем компоненты, плюс готовимся ловить нужные ивенты, передаем пропсы

``` html
<!-- Checkboxes -->
<div class="col col-md-12 col-lg-3">
    <p class="mb-1">Show or not</p>
    <FilterCheckbox v-on:SelectOption="SelectOption" v-for="checkbox in flagOptions" :key="checkbox.id" :name="checkbox.name" :id="checkbox.id" />
</div>
<!-- Container with Tags-->
<div class="col col-md-12 col-lg-6 col-xl-6">
    <p id="tagsHeader" class="mb-1">Tags</p>
    <div class="d-flex flex-row justify-content-between align-content-around flex-wrap h-100">
    <TagButton v-on:SelectTag="SelectOption" v-for="tag in tags" :key="tag.id" :name="tag.name" :id="tag.id"/>
    </div>
</div>
```

## Tag Button

### scripts

Используем emit:

``` javascript
export default {
    name: "TagButton",
    data() {
        return {
            selected: false
        }
    },
    props: {
        name: {
            type: String
        },
        id: {
            type: Number
        }
    },
    methods: {
        SelectTag: function () {
            this.selected = !this.selected
            this.$emit('SelectTag', this.id, 'tag')
        }
    }
}
```

### template

Используем нажатие плюс проверку, что со статусом кнопки

``` html
<template>
    <button type="button" class="btn btn-sm rounded-pill py-0 px-3" :class="{ active: selected, 'btn-secondary': selected, 'btn-light': !selected }" @click="SelectTag"> {{ name }} </button>
</template>
```