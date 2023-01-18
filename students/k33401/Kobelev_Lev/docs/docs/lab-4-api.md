# API

## Auth

### Получение Токена (Вход)

``` javascript
    getAuthToken = async (username, password) => {
        return this.API({
            method: 'POST',
            url: 'auth/token/login/',
            data: {
                username: username,
                password: password
            },
        })
    }
```

### Фетч Пользователя

``` javascript
    fetchUser = async (authToken) => {
        return this.API({
            method: 'GET',
            url: 'auth/users/me/',
            headers: {
                'Authorization': `token ${authToken}`,
            },
        })
    }
```

### Регистрация

``` javascript
    signUp = async (username, password, email) => {
        return this.API({
            method: 'POST',
            url: 'auth/users/',
            data: {
                username: username,
                password: password,
                email: email
            },
        })
    }
```

## Game Systems

### Получение

``` javascript
    getAllGameSystems = async () => {
        return this.API({
            method: 'GET',
            url: 'scenarios/game_systems'
        })
    }
```

## Tags

### Получение

``` javascript
    getAllTags = async () => {
        return this.API({
            method: 'GET',
            url: 'scenarios/tags'
        })
    }
```

## Scenarios

### Получение всех

``` javascript
    getAllScenarios = async (authToken) => {
        if(authToken) {
            return this.API({
                method: 'GET',
                url: 'scenarios/scenarios',
                headers: {
                    'Authorization': `token ${authToken}`,
                }
            })
        }
        return this.API({
            method: 'GET',
            url: 'scenarios/scenarios',
        })
    }
```

### Получение конкретного

``` javascript
    getScenarioById = async (id) => {
        return this.API({
            method: 'GET',
            url: `scenarios/scenarios/${id}`,
        })
    }
```

### Получение фильтрованных

``` javascript
    getFilteredScenarios = async (seacrhParams) => {
        const params = new URLSearchParams();
        for (const [key, value] of Object.entries(seacrhParams)) {
            for (const element of value) {
                params.append(key, element);
            }
        }

        return this.API({
            method: 'GET',
            url: 'scenarios/scenarios',
            params: params
        })
    }
```

### Поставить лайк

``` javascript
    likeScenario = async (id, authToken) => {
        return this.API({
            method: 'PATCH',
            url: `scenarios/scenarios/${id}/likes/update/`,
            headers: {
                'Authorization': `token ${authToken}`,
            },
        })
    }
```

### Создать новый обзор

``` javascript
    likeScenario = async (id, authToken) => {
        return this.API({
            method: 'PATCH',
            url: `scenarios/scenarios/${id}/likes/update/`,
            headers: {
                'Authorization': `token ${authToken}`,
            },
        })
    }
```


## Использование

к методам API обращаются только хранилища, например, 
``` javascript
    async filterScenarios(params) {
            const response = await scenariosAPI.getFilteredScenarios(params)

            this.scenarios = response.data

            return response
    },
```
Способ получение фильтрованных из хранилища сценариев, а вот params приходят уже из компонента.