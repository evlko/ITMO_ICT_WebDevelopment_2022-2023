# Router

``` javascript
import {createRouter, createWebHistory} from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    mode: "history",
    routes: [
        {
            path: '/scenarios',
            name: 'scenarios',
            component: () => import('../views/HomeView.vue')
        },
        {
            path: '/scenarios/:id',
            name: 'scenario',
            component: () => import('../views/ScenarioView.vue'),
            props: true
        }
    ]
})

export default router
```

**NB.** Вход и регистрация — модальные окна, поэтому их нет в роутинге.

## router link

Линков много, например, карточка сценария:

``` html
    <div class="card shadow-sm rounded d-flex flex-column h-100">
        <router-link :to="{name:'scenario', params:{ id: id }}" class="card-body row flex-grow-1 p-0">
            ...
        </router-link>
        ...
    </div>
```