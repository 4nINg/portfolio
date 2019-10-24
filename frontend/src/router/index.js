import Vue from 'vue'
import VueRouter from 'vue-router'

import MainPage from "../components/Main/Views/MainPage"
import SearchPage from "../components/Search/Views/SearchPage"
import EventPage from "../components/Event/Views/EventPage"
import RankPage from "../components/Rank/Views/RankPage"
import LoginPage from "../components/Login/Views/LoginPage"
import searchDetail from "../components/Search/Views/SearchDetailPage.vue"
import AwardPage from "../components/Award/Views/AwardPage";
Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: MainPage, name: 'home' },
        { path: '/search', component: SearchPage, name: 'search' },
        { path: '/event', component: EventPage, name: 'evnet' },
        { path: '/rank', component: RankPage, name: 'rank' },
        { path: '/login', component: LoginPage, name: 'login' },
        { path: '/detail', component: searchDetail, name: 'detail' },
        { path: '/award', component: AwardPage, name: 'award' }

    ],
    scrollBehavior() {
        return { x: 0, y: 0 }
    },
})

export default router