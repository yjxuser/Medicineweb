const PAPER = {
    searchAPI(router, searchtext) {
        if (searchtext !== "") {
            router.push(`/paperresult/${searchtext}`);
        }
    },


}
export default PAPER;