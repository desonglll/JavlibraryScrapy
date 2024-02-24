import {useNavigate, useParams} from "react-router-dom";
import axios from "axios";
import {useEffect, useState} from "react";
import {Card, Spin, Image, Row, Col, Descriptions, DescriptionsProps, Button} from "antd";

export function Detail() {
    const {id} = useParams()
    const instance = axios.create()
    const navigate = useNavigate()
    const [loading, setLoading] = useState(true)
    const [item, setItem] = useState({
        id: "",
        link: "",
        preview: "",
        title: "",
        serial_number: "",
        release_date: "",
        length: "",
        director: "",
        maker: "",
        label: "",
        user_rating: "",
        genres: "",
        cast: "",
        cast_id: "",
        subscribed: "",
        watched: "",
        owned: "",
        preview_thumbs: "",
    })
    const [preview_thumbs, setPreview_thumbs] = useState([])
    const infoItems: DescriptionsProps['items'] = [
        {
            key: 'id',
            label: 'ID',
            children: <p>{item.id}</p>,
        },
        {
            key: 'serial_number',
            label: 'Serial Number',
            children: <p>{item.serial_number}</p>,
            span: 2
        },
        {
            key: 'title',
            label: 'Title',
            children: <p>{item.title}</p>,
        },
        {
            key: 'release_date',
            label: 'Release Date',
            children: <p>{item.release_date}</p>,
        },
        {
            key: 'length',
            label: 'Length',
            children: <p>{item.length}</p>,
        },
        {
            key: 'link',
            label: 'Link',
            children: <a href={item.link}>{item.link}</a>,
        },
        {
            key: 'director',
            label: 'Director',
            children: <p>{item.director}</p>,
        },
        {
            key: 'preview',
            label: 'Preview',
            children: <Image src={item.preview}/>,
        },

        {
            key: 'maker',
            label: 'Maker',
            children: <p>{item.maker}</p>,
        },
        {
            key: 'label',
            label: 'Label',
            children: <p>{item.label}</p>,
        },
        {
            key: 'user_rating',
            label: 'User Rating',
            children: <p>{item.user_rating}</p>,
        },
        {
            key: 'genres',
            label: 'Genres',
            children: <p>{item.genres}</p>,
        },
        {
            key: 'cast',
            label: 'Cast',
            children: <p>{item.cast}</p>,
        },
        {
            key: 'cast_id',
            label: 'Cast ID',
            children: <p>{item.cast_id}</p>,
        },
        {
            key: 'subscribed',
            label: 'Subscribed',
            children: <p>{item.subscribed}</p>,
        },
        {
            key: 'watched',
            label: 'Watched',
            children: <p>{item.watched}</p>,
        },
        {
            key: 'owned',
            label: 'Owned',
            children: <p>{item.owned}</p>,
        },
        {
            key: 'preview_thumbs',
            label: 'Preview Thumbs',
            children: <p>{item.preview_thumbs}</p>,
            span: 2
        },
    ];
    useEffect(() => {
        const fetchData = async () => {
            const res = await instance.get(`api/works/${id}`)
            console.log(res.data)
            const preview_thumbs = res.data["preview_thumbs"].split(", ")
            if (preview_thumbs.length != 0 && preview_thumbs[0] != "") {
                setPreview_thumbs(preview_thumbs)
            }
            setItem(res.data)
        }
        fetchData().then(() => {
            setLoading(!loading)
        })
    }, [])
    return (
        <>
            <Spin spinning={loading}>
                {loading ? (
                    <div>Loading</div>
                ) : (
                    <div>
                        <Button onClick={() => {
                            navigate("/")
                        }}>Home</Button>
                        <Card>{item.title}</Card>
                        <Row style={{display: "flex", flexWrap: "wrap", justifyContent: "center", margin: 20}}>

                            <Col span={16}>
                                {
                                    preview_thumbs.length === 0 ? (
                                        <div></div>
                                    ) : (
                                        <div
                                            style={{display: "flex", flexWrap: "wrap", justifyContent: "flex-start"}}>
                                            <Image.PreviewGroup>
                                                {
                                                    preview_thumbs.map((item, index
                                                    ) => (
                                                        <div key={index} style={{margin: 20, borderRadius: 5}}
                                                        >
                                                            <Image
                                                                width={200}
                                                                height={133}

                                                                src={item}
                                                                style={{borderRadius: 5, objectFit: "cover"}}
                                                            />
                                                        </div>
                                                    ))
                                                }
                                            </Image.PreviewGroup>

                                        </div>
                                    )
                                }
                            </Col>
                            <Col span={8}>
                                <Image src={item.preview} style={{width: "100%"}}/>
                            </Col>
                        </Row>
                        <Descriptions title="Info" bordered items={infoItems}/>
                    </div>
                )}
            </Spin>
        </>
    );
}