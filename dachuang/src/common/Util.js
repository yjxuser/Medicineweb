const Util = {
    searchAPI(router, searchtext) {
        if (searchtext !== "") {
            router.push(`/result/${searchtext}`);
        }
    },


}
export default Util;