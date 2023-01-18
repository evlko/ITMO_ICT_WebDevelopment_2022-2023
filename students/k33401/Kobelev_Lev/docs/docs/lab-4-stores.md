# Stores

## Game Systems

Хранит в себе все системы, используются при фильтрации (компонент чекбокса системы)

``` javascript
const useGameSystemsStore = defineStore('gameSystems', {
    state: () => ({
        gameSystems: [],
    }),
    actions: {
        async loadGameSystems() {
            const response = await gameSystemsAPI.getAllGameSystems()

            this.gameSystems = response.data

            return response
        },
    }
})
```

## Tags

Хранит в себе все тэги, используются при фильтрации (компонент кнопки тэга)

``` javascript
const useTagsStore = defineStore('tags', {
    state: () => ({
        tags: [],
    }),

    actions: {
        async loadTags() {
            const response = await tagsAPI.getAllTags()

            this.tags = response.data

            return response
        },
    }
})
```

## User

Хранит данные юзера

``` javascript
export const useUserStore = defineStore("user", {
    state: () => ({
        authToken: null,
        username: null
    }),

    actions: {
        async fetchUser(authToken) {
            const response = await authAPI.fetchUser(authToken)
            const user = await response
            this.authToken = authToken
            this.username = user.data.username
        },
        async signUp(username, password, email) {
            await authAPI.signUp(username, password, email)

            return this.logIn(username, password)
        },
        async logIn(username, password) {
            const user = await authAPI.getAuthToken(username, password)
            return user
        },
        logOut() {
            this.authToken = null
            this.username = null
        }
    }
})
```

## Scenarios

Хранит **краткие** данные сценариев + **полные** конкретного сценария. 

Взаимодействует с API:
1. Поставить сценарию лайк;
2. Написать отзыв;
3. Сделать фильтр.

Однако сортировка происходит на фронте, так как данных не очень много.

``` javascript
const useScenariosStore = defineStore('scenarios', {
    state: () => ({
        scenarios: [],
        selectedScenario: null,
    }),

    actions: {
        async loadScenarios(authToken) {
            const response = await scenariosAPI.getAllScenarios(authToken)

            this.scenarios = response.data

            return response
        },
        async filterScenarios(params) {
            const response = await scenariosAPI.getFilteredScenarios(params)

            this.scenarios = response.data

            return response
        },
        sortScenarios(key, asc) {
            if (asc) {
                this.scenarios.sort((a, b) => (a[key] > b[key]) ? 1 : ((b[key] > a[key]) ? -1 : 0))
            }
            else {
                this.scenarios.sort((b, a) => (a[key] > b[key]) ? 1 : ((b[key] > a[key]) ? -1 : 0))
            }
        },
        async likeScenario(id, authToken) {
            const response = await scenariosAPI.likeScenario(id, authToken)

            return response
        },
        async loadScenarioById(id) {
            const response = await scenariosAPI.getScenarioById(id)

            this.selectedScenario = response.data

            return response
        },
        async createScenarioReview(text, id, authToken) {
            const response = await scenariosAPI.createScenarioReview(text, id, authToken)

            return response
        }
    }
})
```