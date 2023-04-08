import mutations from "./mutations"
import getters from "./getters"
import actions from "./actions"


export default {
    namespaced: true,
    state(){
        return {
            is_authenticated: false,
            is_admin: false
        }
    },
    mutation: mutations,
    getters: getters,
    actions: actions
}