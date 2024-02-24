import {useEffect, useState} from "react";
import axios from "axios";
import {
    Card,
    Pagination,
    PaginationProps,
    Spin,
    Image,
    Tooltip,
    Form,
    Button,
    Input, Select, Tag,
} from "antd";
import Meta from "antd/es/card/Meta";
import {useNavigate} from "react-router-dom";
import {
    DatabaseOutlined,
    EllipsisOutlined,
    PlayCircleOutlined,
    CopyOutlined,
    CopyFilled,
} from "@ant-design/icons";
import Paragraph from "antd/es/typography/Paragraph";
import FormItem from "antd/es/form/FormItem";

interface Work {
    id?: number;
    link?: string;
    preview?: string;
    title?: string;
    serial_number: string;
    release_date?: string;
    length?: string;
    director?: string;
    maker?: string;
    label?: string;
    user_rating?: string;
    genres?: string | string[];
    cast?: string;
    cast_id?: string;
    subscribed?: string;
    watched?: string;
    owned?: string;
    preview_thumbs?: string;
}

export function Home() {
    const instance = axios.create({});
    const navigate = useNavigate();
    const [items, setItems] = useState([]);
    const [castOptions, setCastOptions] = useState([])
    const [loading, setLoading] = useState(true);
    const [pageSize, setPageSize] = useState(50);
    const [currentPage, setCurrentPage] = useState(1);
    const [totalNumber, setTotalNumber] = useState(0);
    const [castID, setCastID] = useState("%");
    const fetchData = async (
        current: number,
        pageSize: number,
        cast_id = "%",
        cast = "%"
    ) => {
        const res = await instance.get(`api/works`, {
            params: {
                page: current,
                per_page: pageSize,
                cast_id: cast_id,
                cast: cast,
            },
        });

        setItems(res.data);

        res.data.map((item: Work) => {
            if (item.genres) {
                if (typeof item.genres === "string") {
                    item.genres = item.genres.split(',').map(genre => genre.trim());
                }
            }
        });

        const res1 = await instance.get("api/works_table_count");
        setTotalNumber(res1.data["works_table_count"]);

        const cast_options_res = await instance.get("api/actors")
        const cast_options_map = cast_options_res.data.map((item: { cast: string, cast_id: string }) => ({
            value: item.cast_id,
            label: item.cast
        }))
        setCastOptions(cast_options_map)

    };
    useEffect(() => {
        fetchData(currentPage, pageSize).then(() => {
            setLoading(!loading);
        });
    }, []);
    const onShowSizeChange: PaginationProps["onShowSizeChange"] = (
        current,
        pageSize
    ) => {
        setPageSize(pageSize);
        setCurrentPage(current);
        fetchData(current, pageSize, castID).then();
    };
    const handleChange = (item: number) => {
        setCurrentPage(item);
        setPageSize(pageSize);
        fetchData(item, pageSize, castID).then();
    };

    const onFinish = (item: { cast: string; cast_id: string }) => {
        console.log(item);
        if (item.cast === "") {
            item.cast = "%";
        }
        if (item.cast_id === "") {
            item.cast_id = "%";
        }
        setCastID(item.cast_id);
        fetchData(currentPage, pageSize, item.cast_id, item.cast).then();
    };

    return (
        <>
            <Spin spinning={loading} style={{width: "100%"}}>
                {loading ? (
                    <div>Loading</div>
                ) : (
                    <div>
                        <Form
                            onFinish={onFinish}
                            initialValues={{
                                cast_id: "",
                                cast: "",
                            }}
                        >
                            <FormItem name={"cast_id"}>
                                <Select showSearch options={castOptions}
                                        placeholder={"Input cast or cast_id"}
                                        style={{width: 200}}
                                        filterOption={
                                            (input: string, option?: {
                                                label: string;
                                                value: string
                                            }) =>
                                                (option?.label ?? '').toLowerCase().includes(input.toLowerCase()) || (option?.value ?? '').toLowerCase().includes(input.toLowerCase())
                                        }
                                />
                            </FormItem>
                            <FormItem>
                                <Button htmlType={"submit"}>submit</Button>
                            </FormItem>
                        </Form>
                        <Pagination
                            showSizeChanger
                            onShowSizeChange={onShowSizeChange}
                            defaultCurrent={currentPage}
                            total={totalNumber}
                            onChange={(item) => handleChange(item)}
                            showQuickJumper
                        />
                        <div
                            style={{
                                display: "flex",
                                flexWrap: "wrap",
                                justifyContent: "flex-start",
                            }}
                        >
                            {items.map(
                                (item: {
                                    link: string;
                                    id: string;
                                    preview: string;
                                    title: string;
                                    serial_number: string;
                                    release_date: string;
                                    cast: string;
                                    cast_id: string;
                                    genres: string[];
                                }) => (
                                    <Card
                                        key={item.id} // 确保每个元素都有一个唯一的 key
                                        hoverable
                                        style={{width: 240, margin: 10, flex: ""}} // 添加了一些间距
                                        cover={<Image alt="example" src={item.preview}/>} // 使用 item.preview 来引用图片链接
                                        actions={[
                                            <Tooltip title={"MissAV"}>
                                                <a
                                                    href={`https://missav.com/${item.serial_number}`}
                                                    style={{fontSize: 12}}
                                                >
                                                    <PlayCircleOutlined
                                                        key="play"
                                                        style={{margin: 2}}
                                                    />
                                                </a>
                                            </Tooltip>,
                                            <Paragraph
                                                copyable={{
                                                    text: item.cast_id,
                                                    icon: [
                                                        <CopyOutlined key="copy"/>,
                                                        <CopyFilled key="copied"/>,
                                                    ],
                                                    tooltips: ["Copy cast ID", "Copied!!"],
                                                }}
                                            />,
                                            <Tooltip title={"Javlibrary"}>
                                                <a href={item.link}>
                                                    <DatabaseOutlined key="edit"/>
                                                </a>
                                            </Tooltip>,
                                            <EllipsisOutlined key="ellipsis"/>,
                                        ]}
                                    >
                                        <Paragraph
                                            copyable={{
                                                text: item.serial_number,
                                                icon: [
                                                    <CopyOutlined key="copy"/>,
                                                    <CopyFilled key="copied"/>,
                                                ],
                                                tooltips: ["Copy serial number", "Copied!!"],
                                            }}
                                        ></Paragraph>

                                        <div
                                            onClick={() => {
                                                console.log(item.id);
                                                navigate(`works/${item.id}`);
                                            }}
                                        >
                                            <Meta
                                                title={`${item.serial_number}`}
                                                description={`${item.title.slice(0, 25)}`}
                                            />
                                            <br/>
                                            <div>
                                                {item.release_date} {item.cast}
                                            </div>
                                            <div style={{display: "flex", flexWrap: "wrap"}}>{item.genres.map((a) => (
                                                <Tag key={a} style={{margin: 2}}>{a}</Tag>))}</div>
                                        </div>
                                    </Card>
                                )
                            )}
                        </div>
                        <Pagination
                            showSizeChanger
                            onShowSizeChange={onShowSizeChange}
                            defaultCurrent={currentPage}
                            total={totalNumber}
                            onChange={(item) => handleChange(item)}
                            showQuickJumper
                        />
                    </div>
                )}
            </Spin>
        </>
    );
}
