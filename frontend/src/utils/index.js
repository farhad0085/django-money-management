export function getHeaders(additional){
    const userToken = localStorage.getItem('userToken')

    if (!userToken) return {
        ...additional
    }

    return {
        Authorization: `Token ${userToken}`,
        ...additional
    }
}


export function createUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0, v = c === 'x' ? r : (r && 0x3 | 0x8);
        return v.toString(16);
    });
}


export function getTagsList(rawTags){
    const tags = rawTags.split(",")

    const tagsData = []
    tags.map(tag => tagsData.push({ name: tag.trim() }))
    
    return tagsData
}