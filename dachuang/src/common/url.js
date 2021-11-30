const URL = {
    searchAPI(router, searchtext) {
        if (searchtext !== "") {
            router.push(`/urlresult/${searchtext}`);
        }
    },


}
export default URL;