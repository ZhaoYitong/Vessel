/**
 *  const
 */
const VESSEL_IMO = "船舶航次：";
const BAY_INDEX_TIP = "贝位号: ";
/**
 *  variable initialize
 */
let selected_vessel = $(`#vesselSelect option:selected`).val();
/**
 * @classname
 */
/*
    pos_x : bayIndex
    pos_y : rowIndex
    pos_z : layerIndex
 */
/**
 *  data
 */
let VIEW_SIDE = {
    dataType: "",
    bayDirection: "",
    watchType: "sideViewing",
    vessel_id: "001",
    vessel_IMO: "KuiYa123",
    vessel_name: "亚历山大",
    vessel_width: "30m",
    vessel_frontLength: "100m",
    vessel_length: "300m",
    bay_inch20_num: 30,
    max_layer_above_number: 8, // all above
    max_layer_below_number: 5,  // all below
    hatCover_kind: "自开式",
    hatCover_number: 1,
    // create vessel
    vessel: [
        //  down to up
        // below: 02 04 06 08 10
        // above: 82 84 86 88 90 92 94 96 98
        // all: ["01", "03", "05", "07", "09", "11", "13", "15", "17", "19", "21", "23", "25", "27", "29","31", "33", "35", "37", "39", "41", "43", "45", "47", "49","51", "53", "55", "57", "59",],
        // TODO: create a function to solve the value creation:
        // TODO: layer: set left end and right end. Then create bayIndexList and conIndexList
        {
            layerIndex: "02",
            bayIndexList: ["07", "09", "11", "13", "15", "17", "19", "21", "23", "25", "27", "29", "31", "33", "39", "41", "43", "45", "47", "49", "51",],
            conZoneIndexList: ["35", "37"],
        },
        {
            layerIndex: "04",
            bayIndexList: ["05", "07", "17", "19", "49", "51", "53",],
            conZoneIndexList: ["09", "11", "13", "15", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47"],
        },
        {
            layerIndex: "06",
            bayIndexList: ["03", "05", "17", "19", "53", "59"],
            conZoneIndexList: ["07", "09", "11", "13", "15", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49", "51",],

        },
        {
            layerIndex: "08",
            bayIndexList: ["01", "03", "05", "17", "19", "53", "55", "57", "59",],
            conZoneIndexList: ["07", "09", "11", "13", "15", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49", "51",],
        },
        {
            layerIndex: "10",
            bayIndexList: ["01", "03", "17", "19", "57", "59",],
            conZoneIndexList: ["05", "07", "09", "11", "13", "15", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49", "51", "53", "55",],

        },
        {
            layerIndex: "82",
            bayIndexList: ["17", "19"],
            conZoneIndexList: ["01", "03", "05", "07", "09", "11", "13", "15", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49", "51", "53", "55", "57", "59",],

        },
        {
            layerIndex: "84",
            bayIndexList: ["17", "19",],
            conZoneIndexList: ["01", "03", "05", "07", "09", "11", "13", "15", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49", "51", "53", "55", "57", "59",],

        },
        {
            layerIndex: "86",
            bayIndexList: ["17", "19",],
            conZoneIndexList: ["01", "03", "05", "07", "09", "11", "13", "15", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49", "51", "53", "55", "57", "59",],

        },
        {
            layerIndex: "88",
            bayIndexList: ["17", "19",],
            conZoneIndexList: ["01", "03", "05", "07", "09", "11", "13", "15", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49", "51", "53", "55", "57", "59",],

        },
        {
            layerIndex: "90",
            bayIndexList: ["17", "19",],
            conZoneIndexList: ["01", "03", "05", "07", "09", "11", "13", "15", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49", "51", "53", "55", "57", "59",],

        },
        {
            layerIndex: "92",
            bayIndexList: ["17",],
            conZoneIndexList: ["01", "03", "05", "07", "09", "11", "13", "15", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49", "51", "53", "55", "57", "59",],

        },
        {
            layerIndex: "94",
            bayIndexList: [],
            // conZoneIndexList: ["01", "03", "05", "07", "09", "11", "13", "15", "21", "23", "25", "27", "29","31", "33", "35", "37", "39", "41", "43", "45", "47", "49","51", "53", "55", "57", "59",],
            conZoneIndexList: [],
        },
        {
            layerIndex: "96",
            bayIndexList: [],
            // conZoneIndexList: ["01", "03", "05", "07", "09", "11", "13", "15", "21", "23", "25", "27", "29","31", "33", "35", "37", "39", "41", "43", "45", "47", "49","51", "53", "55", "57", "59",],
            conZoneIndexList: [],
        },

    ],
    // 舱盖板
    typeOfBoard: "",
    numOfBoard: 1,
};
let vesselStorageInfoAll = {
    dataType: "VESSEL_STORAGE_INFO",
    vessel_id: "001",
    vessel_IMO: "KuiYa123",
    data: [
        {
            id: 1,
            type: "single",
            bayInch20: [
                {
                    index: "01",
                    layerList: [],
                }
            ],
        },
        {
            id: 2,
            type: "combine",
            bayInch20s: [
                {
                    index: "03",
                },
                {
                    index: "05",
                },
            ],
            bayInch40: [
                {
                    index: "04",
                },
            ],
        },
        {
            id: 3,
            type: "single",
            bayInch20: [
                {
                    index: "07",
                }
            ],
        },
        {
            id: 4,
            type: "combine",
            bayInch20s: [
                {
                    index: "09",
                },
                {
                    index: "11",
                },
            ],
            bayInch40: [
                {
                    index: "10",
                },
            ],
        },
        {
            id: 5,
            type: "combine",
            bayInch20s: [
                {
                    index: "13",
                },
                {
                    index: "15",
                },
            ],
            bayInch40: [
                {
                    index: "14",
                },
            ],
        },
        {
            id: 6,
            type: "single",
            bayInch20: [
                {
                    index: "17",
                }
            ],
        },
        {
            id: 7,
            type: "single",
            bayInch20: [
                {
                    index: "19",
                }
            ],
        },
        {
            id: 8,
            type: "single",
            bayInch20: [
                {
                    index: "21",
                }
            ],
        },
        {
            id: 9,
            type: "single",
            bayInch20: [
                {
                    index: "23",
                }
            ],
        },
        {
            id: 10,
            type: "single",
            bayInch20: [
                {
                    index: "25",
                }
            ],
        },
        {
            id: 11,
            type: "single",
            bayInch20: [
                {
                    index: "27",
                }
            ],
        },
        {
            id: 12,
            type: "combine",
            bayInch20s: [
                {
                    index: "29",
                },
                {
                    index: "31",
                },
            ],
            bayInch40: [
                {
                    index: "30",
                },
            ],
        },
        {
            id: 13,
            type: "combine",
            bayInch20s: [
                {
                    index: "33",
                },
                {
                    index: "35",
                },
            ],
            bayInch40: [
                {
                    index: "34",
                },
            ],
        },
        {
            id: 14,
            type: "combine",
            bayInch20s: [
                {
                    index: "37",
                },
                {
                    index: "39",
                },
            ],
            bayInch40: [
                {
                    index: "38",
                },
            ],
        },
        {
            id: 15,
            type: "single",
            bayInch20: [
                {
                    index: "41",
                }
            ],
        },
        {
            id: 16,
            type: "single",
            bayInch20: [
                {
                    index: "43",
                }
            ],
        },
        {
            id: 17,
            type: "single",
            bayInch20: [
                {
                    index: "45",
                }
            ],
        },
        {
            id: 18,
            type: "single",
            bayInch20: [
                {
                    index: "47",
                }
            ],
        },
        {
            id: 19,
            type: "single",
            bayInch20: [
                {
                    index: "49",
                }
            ],
        },
        {
            id: 20,
            type: "single",
            bayInch20: [
                {
                    index: "51",
                }
            ],
        },
        {
            id: 21,
            type: "combine",
            bayInch20s: [
                {
                    index: "53",
                },
                {
                    index: "55",
                },
            ],
            bayInch40: [
                {
                    index: "54",
                },
            ],
        },
        {
            id: 22,
            type: "single",
            bayInch20: [
                {
                    index: "57",
                }
            ],
        },
        {
            id: 23,
            type: "single",
            bayInch20: [
                {
                    index: "59",
                }
            ],
        },
    ],
};

/**
 * custom function
 */
// id number to string
function numToIdString(num) {
    return num < 10 ? "0" + num.toString() : num.toString();
}

// is exist in array (str)
function isExist(array, value) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === value) {
            return true;
        }
    }
    return false;
}

function toAbsent(value) {
    return value > 0 ? value : -value;
}

function directionDealer(num, dir, func, isInverse) {
    // set isInverse as args to control
    if (isInverse) {
        if (dir === 'L') {
            for (let a = 0; a < num; a++) {
                func(a, dir);
            }
        } else {
            for (let b = num - 1; b >= 0; b--) {
                func(b, dir);
            }
        }
    } else {
        if (dir === 'L') {
            for (let d = num - 1; d >= 0; d--) {
                func(d, dir);
            }
        } else {
            for (let c = 0; c < num; c++) {
                func(c, dir);
            }
        }
    }
}

// zoom in and zoom out
function setZoom(zoom, el) {
    let transformOrigin = [0, 0];
    el = el || instance.getContainer();
    let p = ["webkit", "moz", "ms", "o"],
        s = "scale(" + zoom + ")",
        oString = (transformOrigin[0] * 100) + "% " + (transformOrigin[1] * 100) + "%";
    for (let i = 0; i < p.length; i++) {
        el.style[p[i] + "Transform"] = s;
        el.style[p[i] + "TransformOrigin"] = oString;
    }
    el.style["transform"] = s;
    el.style["transformOrigin"] = oString;
}

function showVal(a) {
    let zoomScale = Number(a) / 10;
    setZoom(zoomScale, document.getElementsByClassName('mainArea')[0])
}

/**
 *  initialize bay area
 */
function BayNumToRealIndexList(bayNum) {
    let bay = {};
    bay.inch20 = [];
    for (let i = 0; i < bayNum; i++) {
        bay.inch20[i] = {
            "id": i + 1,
            "bayRealIndex": numToIdString(i * 2 + 1)
        };
    }
    return bay;
}

// layer above
// layer below
function layerNumToRealIndexList(layerNumAbove, layerNumBelow) {
    let layer = {};
    layer.above = [];
    layer.below = [];
    for (let i = 0; i < layerNumAbove; i++) {
        layer.above[i] = {
            id: i + 1,
            layerRealIndex: numToIdString((i + 41) * 2),
        }
    }
    for (let j = 0; j < layerNumBelow; j++) {
        layer.below[j] = {
            id: j + 1,
            layerRealIndex: numToIdString((j + 1) * 2),
        }
    }
    return layer;
}

function createBayCombinationInfo(newList) {
    let newBay_num = newList.data.length;
    let dataList = newList.data;
    let dir = newList.bayDirection;
    // TODO: func to createLoadOrUnloadInfo
    let drawNewBay = function (index, bay_dir) {
        let itemId = dataList[index].id;
        if (dataList[index].type === "single") {
            let bayIndex = dataList[index].bayInch20[0].index;
            $(`.newBayArea`)
                .append(`<div id= ${itemId} bay_index=${bayIndex} class="newBay20 bay-20">` +
                `<span class="newBay20Index">${dataList[index].bayInch20[0].index}</span>` +
                `</div>`);
        } else {
            if (bay_dir === 'R') {
                let bay40_index = dataList[index].bayInch40[0].index;
                let bay20_left = dataList[index].bayInch20s[1].index;
                let bay20_right = dataList[index].bayInch20s[0].index;
                $(`.newBayArea`).append(`<div id= ${itemId} class="comBay20_40">` +
                    `<div class="newBay40InCom bay-40">` +
                    `<span class="newBay40IndexInCom">${bay40_index}</span>` +
                    `</div>` +
                    `<div class="newBay20InComParent">` +
                    `<div class="newBay20InComLeft bay-20">` +
                    `<span class="newBay20IndexInCom">${bay20_left}</span></div>` +
                    `<div class="newBay20InComRight bay-20">` +
                    `<span class="newBay20IndexInCom">${bay20_right}</span></div>` +
                    `</div>` +
                    `</div>`);
            } else {
                // bay_dir === 'L'
                let bay40_index = dataList[index].bayInch40[0].index;
                let bay20_left = dataList[index].bayInch20s[0].index;
                let bay20_right = dataList[index].bayInch20s[1].index;
                $(`.newBayArea`).append(`<div id= ${itemId} class="comBay20_40">` +
                    `<div class="newBay40InCom bay-40">` +
                    `<span class="newBay40IndexInCom">${bay40_index}</span>` +
                    `</div>` +
                    `<div class="newBay20InComParent">` +
                    `<div class="newBay20InComLeft bay-20">` +
                    `<span class="newBay20IndexInCom">${bay20_left}</span></div>` +
                    `<div class="newBay20InComRight bay-20">` +
                    `<span class="newBay20IndexInCom">${bay20_right}</span></div></div>` +
                    `</div>`);
            }
        }
    };
    let isInverse = true;
    directionDealer(newBay_num, dir, drawNewBay, isInverse);
    $(`.bay-20`).on('click', function () {
        let index = this.childNodes[0].innerText;
        let ves_selected = $(`#vesselSelect option:selected`).val();
        $.ajax({
            url: '/vesselStruct/define_bay_struct/',
            type: 'GET',
            data: {
                name: ves_selected,
                index: index,
            },
            dataType: "json",
            success: function (res) {
                // console.log(res);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(XMLHttpRequest.status);
            },
        });
    });
    $(`[class="newBay20"][id="6"]`).addClass("blink");
    $(`[class="newBay20"][id="7"]`).addClass("blink");
}

/**
 *  vessel creation
 */
function createVesselSide() {
    // $(`.createVessel`)[0].disabled = true;
    if ($(`.vesselAreaSide`)) {
        $(`.vesselAreaSide`).empty();
    }
    $.ajax({
        url: '/vesselStruct/ves_struct/',
        type: 'GET',
        data: {
            name: selected_vessel,
        },
        dataType: "json",
        success: function (res) {
            // console.log(res);
            let bay_num = res.bay_inch20_num;
            let layerNumAbove = res.max_layer_above_number;
            let layerNumBelow = res.max_layer_below_number;
            let dir = res.bayDirection;
            let eng_list_ind = res.engine_room_index;
            drawVesselStruct(bay_num, layerNumAbove, layerNumBelow, dir, eng_list_ind)
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(XMLHttpRequest.status);
        },
    });
}

function drawVesselStruct(bay_num, lay_above_num, lay_below_num, dir, engine_list) {
    let bayLists = BayNumToRealIndexList(bay_num);
    let layerLists = layerNumToRealIndexList(lay_above_num, lay_below_num);
    let conZone_bay_num = bayLists.inch20.length;
    let conZone_layerAbove_num = layerLists.above.length;
    let conZone_layerBelow_num = layerLists.below.length;
    let eng_list_index = engine_list;
    // initial above and below
    $(`.vesselAreaSide`).append(`<div class="onBoardSide"></div>`)
        .append(`<div class="belowBoardSide"></div>`);
    // TODO: change conZoneAbove_inch20 according maxLayer input
    // TODO: tip1: set fixed height according maxLayer input
    let drawVesBayArea = function (index, args_dir) {
        let conZoneBayIndex = bayLists.inch20[index].bayRealIndex;
        $(`.onBoardSide`).append(`<div pos_x=${conZoneBayIndex} class="bayAbove_20"></div>`);
        $(`.belowBoardSide`).append(`<div pos_x=${conZoneBayIndex} class="bayBelow_20"></div>`);
    };
    let isInverse = true;
    directionDealer(conZone_bay_num, dir, drawVesBayArea, isInverse);
    // zone: bay + layer
    for (let j = 0; j < conZone_bay_num; j++) {
        let conZoneBayIndex = bayLists.inch20[j].bayRealIndex;
        for (let k = conZone_layerAbove_num - 1; k >= 0; k--) {
            let conZoneLayerIndex = layerLists.above[k].layerRealIndex;
            let item = `<div class="conZone_20" p_x=${conZoneBayIndex} p_z=${conZoneLayerIndex}></div>`;
            $(`.onBoardSide div[pos_x=${conZoneBayIndex}]`).append(item);
        }
        for (let m = conZone_layerBelow_num - 1; m >= 0; m--) {
            let conZoneLayerIndex = layerLists.below[m].layerRealIndex;
            let item = `<div class="conZone_20" p_x=${conZoneBayIndex} p_z=${conZoneLayerIndex}></div>`;
            $(`.belowBoardSide div[pos_x=${conZoneBayIndex}]`).append(item);
        }
    }
    // css control ves body, engine, and container zone
    $(`.bayAbove_20`).children('div').addClass("vessel_inch20_default");
    $(`.bayBelow_20`).children('div').addClass("vessel_inch20_default");
    // console.log(eng_list_index);
    for (let i = 0; i < eng_list_index.length; i++) {
        let index = eng_list_index[i].toString();
        // console.log(index);
        $(`div[p_x=${index}]`).addClass("vesselBody_inch20");
    }
}

/**
 *  stowage info
 */
function createStowageInfo() {
    // $(`.createStowage`)[0].disabled = true;
    if ($(`div[class="vesselStowageInfo"]`)) {
        $(`div[class="vesselStowageInfo"]`).empty();
    }
    let selected_ves = $(`#vesselSelect option:selected`).val();
    $.ajax({
        url: '/vesselStruct/stowage_info/',
        type: 'GET',
        data: {
            name: selected_ves,
        },
        dataType: "json",
        success: function (res) {
            console.log(res);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(XMLHttpRequest.status);
        },
    });


    let header = vesselStorageInfoAll.vessel_IMO;
    let bayNum = vesselStorageInfoAll.data.length;
    let ves_header = `<div class="vesselHeader">`+
        `<span class="stowageInfoHeader">${VESSEL_IMO}${header}</span></div>`;
    let ves_bay_stowage_area = `<div class="baysStowageArea"></div>`;
    $(`.vesselStowageInfo`).append(ves_header).append(ves_bay_stowage_area);
    let item_bay_info = function (tip, bayIndex) {
        return `<div id="${bayIndex}" class="bayStowage"><div class="header"><span>${tip}${bayIndex}</span></div><div class="content"></div></div>`
    };
    for (let i = 0; i < bayNum; i++) {
        let itemType = vesselStorageInfoAll.data[i].type;
        if (itemType === "single") {
            let bayIndexOfBay = vesselStorageInfoAll.data[i].bayInch20[0].index;
            $(`.baysStowageArea`).append(item_bay_info(BAY_INDEX_TIP, bayIndexOfBay));
        } else {
            // itemType === "combine"
            let tempBayIndexOfBay_0 = vesselStorageInfoAll.data[i].bayInch20s[0].index;
            let bayIndexOfBay_1 = vesselStorageInfoAll.data[i].bayInch20s[1].index;
            let bayIndexOfBay_con = vesselStorageInfoAll.data[i].bayInch40[0].index;
            let bayIndexOfBay_0 = tempBayIndexOfBay_0 + "(" + bayIndexOfBay_con + ")";
            $(`.baysStowageArea`)
                .append(item_bay_info(BAY_INDEX_TIP, bayIndexOfBay_0))
                .append(item_bay_info(BAY_INDEX_TIP, bayIndexOfBay_1));
        }
    }
}

function drawVesselPending(new_bay_num, bayList, dir, dataList, engine_list) {
    // initial div above and below
    $(`.vesOperationInfo`).append(`<div class="above"></div>`)
        .append(`<div class="board"></div>`).append(`<div class="below"></div>`);
    $(`div[class="vesOperationInfo"] div[class="above"]`)
        .append(`<div class="operationInch40Num"></div>`)
        .append(`<div class="unload"></div>`)
        .append(`<div class="load"></div>`)
        .append(`<div class="operationInch20Num"></div>`);
    $(`div[class="vesOperationInfo"] div[class="below"]`)
        .append(`<div class="unload"></div>`).append(`<div class="load"></div>`);

    function draw_single_row(pos, op_type, bay_list, index, dir) {
        // add class: above or below, load or unload
        let position = 'ves_' + pos;
        let type = 'ves_' + op_type;
        if (bay_list[index].type === "single") {
            let bayIndex = bayList[index].bayInch20[0].index;
            $(`div[class = ${pos}] div[class=${op_type}]`)
                .append(`<div id=${bayIndex} class="bay_20 ${position} ${type}">` +
                    `<span class="text_silver"></span></div>`);
        } else {
            if (dir === 'R') {
                let bay_40 = bayList[index].bayInch40[0].index;
                let left_index = bayList[index].bayInch20s[1].index;
                let right_index = bayList[index].bayInch20s[0].index;
                $(`div[class = ${pos}] div[class=${op_type}]`).append(`<div class="comBay">` +
                    `<div id=${bay_40} class="bay40InCom ${position} ${type}">` +
                    `<span class="text_silver"></span></div><div class="bay20sInCom">` +
                    `<div id=${left_index} class="bay20InComLeft ${position} ${type}">` +
                    `<span class="text_silver"></span></div>` +
                    `<div id=${right_index} class="bay20InComRight ${position} ${type}">` +
                    `<span class="text_silver"></span></div>` +
                    `</div></div>`);
            } else {
                // dir === 'L'
                let bay_40 = bayList[index].bayInch40[0].index;
                let left_index = bayList[index].bayInch20s[0].index;
                let right_index = bayList[index].bayInch20s[1].index;
                $(`div[class = ${pos}] div[class=${op_type}]`).append(`<div class="comBay">` +
                    `<div id=${bay_40} class="bay40InCom ${position} ${type}">` +
                    `<span class="text_silver"></span></div><div class="bay20sInCom">` +
                    `<div id=${left_index} class="bay20InComLeft ${position} ${type}">` +
                    `<span class="text_silver"></span></div>` +
                    `<div id=${right_index} class="bay20InComRight ${position} ${type}">` +
                    `<span class="text_silver"></span></div>` +
                    `</div></div>`);
            }
        }

    }

    let drawConsPending = function (key, args_dir) {
        draw_single_row("above", "unload", bayList, key, args_dir);
        draw_single_row("above", "load", bayList, key, args_dir);
        draw_single_row("below", "unload", bayList, key, args_dir);
        draw_single_row("below", "load", bayList, key, args_dir);
    };
    let isInverse = true;
    directionDealer(new_bay_num, dir, drawConsPending, isInverse);
    // TODO: add data to area
    // console.log(dataList);
    for (let i = 0; i < dataList.inch20.length; i++) {
        let index = dataList.inch20[i].index;
        let val_above_load = dataList.inch20[i].data.above_load;
        let val_above_unload = dataList.inch20[i].data.above_unload;
        let val_below_load = dataList.inch20[i].data.below_load;
        let val_below_unload = dataList.inch20[i].data.below_unload;
        $(`div[class="above"] div[class="load"] div[id=${index}] span`)[0].innerText = val_above_load;
        $(`div[class="above"] div[class="unload"] div[id=${index}] span`)[0].innerText = val_above_unload;
        $(`div[class="below"] div[class="load"] div[id=${index}] span`)[0].innerText = val_below_load;
        $(`div[class="below"] div[class="unload"] div[id=${index}] span`)[0].innerText = val_below_unload;
    }
    for (let j = 0; j < dataList.inch40.length; j++) {
        let index = dataList.inch40[j].index;
        let val_above_load = dataList.inch40[j].data.above_load;
        let val_above_unload = dataList.inch40[j].data.above_unload;
        let val_below_load = dataList.inch40[j].data.below_load;
        let val_below_unload = dataList.inch40[j].data.below_unload;
        $(`div[class="above"] div[class="load"] div[id=${index}] span`)[0].innerText = val_above_load;
        $(`div[class="above"] div[class="unload"] div[id=${index}] span`)[0].innerText = val_above_unload;
        $(`div[class="below"] div[class="load"] div[id=${index}] span`)[0].innerText = val_below_load;
        $(`div[class="below"] div[class="unload"] div[id=${index}] span`)[0].innerText = val_below_unload;
    }
    // $(`div[class="above"] div[class="unload"] div[id="69"] span`)[0].innerText = 10;

    // engine_body
    for (let k = 0; k < engine_list.length; k++) {
        // console.log(typeof engine_list[k]);
        let index = engine_list[k].toString();
        $(`div[class="above"] div[class="load"] div[id=${index}]`).addClass("engineBody").children("span")[0].innerText = null;
        $(`div[class="above"] div[class="unload"] div[id=${index}]`).addClass("engineBody").children("span")[0].innerText = null;
        $(`div[class="below"] div[class="load"] div[id=${index}]`).addClass("engineBody").children("span")[0].innerText = null;
        $(`div[class="below"] div[class="unload"] div[id=${index}]`).addClass("engineBody").children("span")[0].innerText = null;
    }
}

function createLoadOrUnloadInfo() {
    // $(`.createLoadOrUnload`)[0].disabled = true;
    if ($(`div[class="vesOperationInfo"]`)) {
        $(`div[class="vesOperationInfo"]`).empty();
    }
    let selected_ves = $(`#vesselSelect option:selected`).val();
    $.ajax({
        url: '/vesselStruct/con_pend_info/',
        type: 'GET',
        data: {
            name: selected_ves,
        },
        dataType: "json",
        success: function (res) {
            // console.log(res);
            let new_bay_num = res.bay_list.length;
            let bay_list = res.bay_list;
            let dir = res.bayDirection;
            let data_list = res.data_list;
            let engBodyList = res.engineRoomIndex;
            drawVesselPending(new_bay_num, bay_list, dir, data_list, engBodyList);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(XMLHttpRequest.status);
        },
    });
}

/**
 *  combination buttons
 */
function getCombineInfo() {
    if ($(`.newBayArea`)) {
        $(`.newBayArea`).empty();
    }
    selected_vessel = $(`#vesselSelect option:selected`).val();
    $.ajax({
        url: '/vesselStruct/edit_bay/',
        type: 'GET',
        data: {
            name: selected_vessel,
            type: 'current_info',
        },
        dataType: "json",
        success: function (res) {
            // console.log(res);
            createBayCombinationInfo(res);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(XMLHttpRequest.status);
        },
    });
}

/**  all bays struct of vessel **/
function createAllBaysStruct(){
    if($(`.allBaysStruct`)){
        $(`.allBaysStruct`).empty();
    }
    let selected_ves = $(`#vesselSelect option:selected`).val();
    $.ajax({
        url: '/vesselStruct/all_bays_struct/',
        type: 'GET',
        data: {
            name: selected_ves,
            type: 'bays_info',
        },
        dataType: "json",
        success: function (res) {
            console.log(res);
            drawAllBayStruct(res);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(XMLHttpRequest.status);
        },
    });
}
function drawAllBayStruct(res){
    let header = res.ves_name;
    let content = res.content;
    let ves_header = `<div class="vesselHeader">`+
        `<span class="baysStructInfoHeader">${VESSEL_IMO}${header}</span></div>`;
    let ves_bay_stowage_area = `<div class="baysStructArea"></div>`;
    $(`.allBaysStruct`).append(ves_header).append(ves_bay_stowage_area);
    let item_bay_info = function (tip, bayIndex) {
        return `<div id="${bayIndex}" class="bayStruct"><div class="header"><span>${tip}${bayIndex}</span></div><div class="bay-struct-content" bay_index=${bayIndex}></div></div>`
    };
    for (let i = 0; i < content.length; i++) {
        let bay_index = content[i].bay_index;
        $(`.baysStructArea`).append(item_bay_info(BAY_INDEX_TIP, bay_index));
        drawBayStruct(content[i]);
    }
}
// draw single bay struct
function getDeckLayIndex(real, max) {
    let temp=[];
    for(let i=0; i<(real? real:max);i++){
        temp.push(numToIdString((41+i)*2));
    }
    // console.log("deckBayIndex: " + temp);
    return temp;
}
function getCabLayIndex(real, max) {
    let temp =[];
    for(let j=0; j<(real? real:max); j++) {
        temp.push(numToIdString((j+1)*2));
    }
    // console.log("cabBayIndex: " + temp);
    return temp;
}
function createColIndex(num_of_col) {
    let temp_list = [];
    if (num_of_col%2 === 0){
        // 00 line
        let sub = num_of_col/2;
        for(let i=sub; i>0; i--){
            temp_list.push(numToIdString(i*2));
        }
        for(let j=0; j<sub; j++){
            temp_list.push(numToIdString((j+1)*2-1));
        }
    }
    else {
        let sub = (num_of_col-1)/2;
        for(let i=sub; i>0; i--){
            temp_list.push(numToIdString(i*2));
        }
        temp_list.push('00');
        for(let j=0; j<sub; j++){
            temp_list.push(numToIdString((j+1)*2-1));
        }
    }
    // console.log("colIndex: " + temp_list);
    return temp_list;
}
function drawBayStruct(item) {
    // item in content
    // let ves_name = item.ves_name;
    let bay_index = item.bay_index;
    let deck_max_lay = item.bay_struct_max.deck_lay_num_max;
    let cab_max_lay = item.bay_struct_max.cab_lay_num_max;
    let deck_max_col = item.bay_struct_max.deck_col_num_max;
    let cab_max_col = item.bay_struct_max.cab_col_num_max;

    let deck_real_lay = item.real_bay_struct.deck_lay_num_real;
    let cab_real_lay = item.real_bay_struct.cab_lay_num_real;
    let cab_real_col = item.real_bay_struct.cab_col_num_real;
    let deck_real_col = item.real_bay_struct.deck_col_num_real;

    let bay_layer_con_zone = item.bay_layer_con_zone;

    // create bay-structure
    $( `div[class="bay-struct-content"][bay_index=${bay_index}]`).append(`<div class="bay-struct-define">`+
    // `<div class="bay-struct-header" bay_index=${bay_index} name="bay-index">`+
    //     `<span></span>`+
    // `</div>`+
    `<div class="bay-struct-content" name="bay-struct-area">`+
        `<div class="bay-col-index-deck">`+
            `<div class="blank-index-deck"></div>`+
            `<div class="col-index-area-deck" bay_index=${bay_index}></div>`+
        `</div>`+
        `<div class="bay-deck-lays" bay_index=${bay_index}></div>`+
        `<div class="vessel-hat">`+
            `<div class="blank-hat-area"></div>`+
            `<div class="hat-area"></div>`+
        `</div>`+
        `<div class="bay-cab-lays" bay_index=${bay_index}></div>`+
        `<div class="bay-col-index-cab">`+
            `<div class="blank-index-cab"></div>`+
            `<div class="col-index-area-cab" bay_index=${bay_index}></div>`+
        `</div>`+
    `</div>`+
    `</div>`);

    let lay_index_deck = getDeckLayIndex(deck_real_lay,deck_max_lay);
    let lay_index_cab = getCabLayIndex(cab_real_lay,cab_max_lay);

    let col_index_deck_list = createColIndex(deck_real_col? deck_real_col:deck_max_col);
    let col_index_cab_list = createColIndex(cab_real_col? cab_real_col:cab_max_col);

    // from up to down
    // $(`div[class="bay-struct-header"][bay_index=${bay_index}]`).children()[0].innerText = '贝位号: '+ bay_index;
    // col-index on deck
    for(let k=0; k<col_index_deck_list.length; k++){
        let col_index = col_index_deck_list[k];
        $(`div[class="col-index-area-deck"][bay_index=${bay_index}]`).append(`<div class="col-index-zone">${col_index}</div>`);
    }
    for(let r=0; r<col_index_cab_list.length; r++){
        let col_index = col_index_cab_list[r];
        $(`div[class="col-index-area-cab"][bay_index=${bay_index}]`).append(`<div class="col-index-zone">${col_index}</div>`);
    }
    //lay
    for(let m=lay_index_deck.length-1; m>=0; m--){
        let lay_index = lay_index_deck[m];
        $(`div[class="bay-deck-lays"][bay_index=${bay_index}]`).append(`<div class="bay-deck-single-lay"><div class="bay-lay-index">${lay_index}</div><div class="bay-lay-zones" layer=${lay_index} bay_index=${bay_index}></div></div>`);
        for(let n=0; n<col_index_deck_list.length; n++){
            let col_index = col_index_deck_list[n];
            if(bay_layer_con_zone.length === 0) {
                $(`div[layer=${lay_index}][bay_index=${bay_index}]`).append(`<div class="con-zone-initial" pos_x=${bay_index} pos_y=${col_index} pos_z=${lay_index}></div>`);
            }
            else {
                $(`div[layer=${lay_index}][bay_index=${bay_index}]`).append(`<div class="con-zone-after" pos_x=${bay_index} pos_y=${col_index} pos_z=${lay_index}></div>`);
            }
        }
    }
    for(let p=lay_index_cab.length-1; p>=0; p--){
        let lay_index = lay_index_cab[p];
        $(`div[class="bay-cab-lays"][bay_index=${bay_index}]`).append(`<div class="bay-cab-single-lay"><div class="bay-lay-index">${lay_index}</div><div class="bay-lay-zones" layer=${lay_index} bay_index=${bay_index}></div></div>`);
        for(let q=0; q<col_index_cab_list.length; q++){
            let col_index = col_index_cab_list[q];
            if(bay_layer_con_zone.length === 0) {
                $(`div[layer=${lay_index}][bay_index=${bay_index}]`).append(`<div class="con-zone-initial" pos_x=${bay_index} pos_y=${col_index} pos_z=${lay_index}></div>`);
            }
            else {
                $(`div[layer=${lay_index}][bay_index=${bay_index}]`).append(`<div class="con-zone-after" pos_x=${bay_index} pos_y=${col_index} pos_z=${lay_index}></div>`);
            }
        }
    }
    // show real con-zone if exist
    if(bay_layer_con_zone.length !== 0) {
         for (let i = 0; i < bay_layer_con_zone.length; i++) {
             let lay_index = bay_layer_con_zone[i].layer_index;
             let con_list = bay_layer_con_zone[i].con_zone_list;
             for (let j=0; j<con_list.length; j++){
                 let pos_y = col_index_deck_list[j];
                 if(con_list[j] === '1'){
                     $(`div[class="con-zone-after"][pos_z=${lay_index}][pos_y=${pos_y}][pos_x=${bay_index}]`).addClass("con-zone-exist");
                 }
             }
         }
    }
}

// TODO: add engine after combination of bay
/**
 *  test area
 */
// TODO: CUSTOM BLINK TRICK
$(`[pos_x="19"],[pos_x="17"]`).addClass("blink");